from ast import *
from queue import Full
from random import choice
from numpy import *

def MKDeck ():
	Suit=["H","D","S","C"]
	Deck=[]
	for S in Suit:
		for x in range(13):
			if x == 10:
				Deck.append(S+"J")
			elif x==11:
				Deck.append(S+"Q")
			elif x==12:
				Deck.append(S+"K")
			elif x==0:
				Deck.append(S+"A")
			else:
				Deck.append(S+str(x+1))
	return Deck

def MKShoe(NumOfDeck):
	Shoe=[]
	for x in range(NumOfDeck):
		Deck=MKDeck()
		for D in Deck:
			Shoe.append(D)
	return Shoe

def Swap(Array):
	RandNum1 = random.randint(len(Array)-1)
	RandNum2 = random.randint(len(Array)-1)
	temp=Array[RandNum1]
	Array[RandNum1]=Array[RandNum2]
	Array[RandNum2]=temp
	return Array

def ShuffleShoe(Shoe1):
	for x in Shoe1:
		Shoe1=Swap(Shoe1)
	return Shoe1

def HandAdd(Pts):
	Total=0
	for x in Pts:
		Total+=x
	return Total

def PointCheck(Hand):
	Points=[]
	NumTest=[2,3,4,5,6,7,8,9,10]
	LetterTest=["J","Q","K"]
	for x in range(len(Hand)):
		Points.append(0)
		for N in NumTest:
			if str(N) in Hand[x]:
				Points[x]=N
		for L in LetterTest:
			if L in Hand[x]:
				Points[x]=10
	for x in range(len(Hand)):
		if "A" in Hand[x]:
			Points[x]=11
			if HandAdd(Points)>21:
				Points[x]=1			
	return Points

def Draw(Hand1):
	Hand1.append(Full_Deck[0])
	Full_Deck.pop(0)

def DisplayTable():
	print("=======================")
	print("Dealer:")
	print(DealerHand)
	print("  Total:"+str(HandAdd(PointCheck(DealerHand))))
	print("")
	print("Player:")
	print(PlayerHand)
	print("  Total:"+str(HandAdd(PointCheck(PlayerHand))))

def RunStand():
	while HandAdd(PointCheck(DealerHand)) < 17:
		Draw(DealerHand)
	if HandAdd(PointCheck(DealerHand)) > 21:
		DisplayTable()
		print("")
		print("||============================||")
		print("||Congratualtion! Dealer Busts||")
		print("||============================||")
	elif HandAdd(PointCheck(DealerHand)) > HandAdd(PointCheck(PlayerHand)):
		DisplayTable()
		print("")
		print("||===================||")
		print("||Sorry, Dealer Wins!||")
		print("||===================||")
	elif HandAdd(PointCheck(DealerHand)) < HandAdd(PointCheck(PlayerHand)):
		DisplayTable()
		print("")
		print("||=========================||")
		print("||Congratualtion!, You Win!||")
		print("||=========================||")
	elif HandAdd(PointCheck(DealerHand)) == HandAdd(PointCheck(PlayerHand)):
		DisplayTable()
		print("")
		print("||================||")
		print("||Push!, You Tied!||")
		print("||================||")
		
def Round():
	Choice=0
	for x in range(2):
		Draw(PlayerHand)
		Draw(DealerHand)
	
	while Choice==0:
		if HandAdd(PointCheck(PlayerHand)) <= 21:
			DisplayTable()
			print("")
			print("'H'it or 'S'tand")
			Answer=input()
			if ("S" in Answer or "s" in Answer):
				Choice=1
				RunStand()
			elif ("H" in Answer or "h" in Answer):
				Draw(PlayerHand)
				continue
			else:
				print("")
		else:
			DisplayTable()
			print("||==============||")
			print("||Sorry you bust||")
			print("||==============||")
			Choice=1

def StartGame(Deck):
	Choice=0
	while Choice==0:
		if len(Deck)<=(10):
			print("Hold on one second dealer has to reshuffle the deck of cards")
			Full_Deck=MKShoe(DS)
			Full_Deck=ShuffleShoe(Full_Deck)
		
		Round()
		print("")
		print("Would you like play another round?")
		Answer=input()
		PlayerHand.clear()
		DealerHand.clear()
		if "N" in Answer or "n" in Answer:
			Choice=1
			print("Come Back Soon!")
		else:
			continue

PlayerHand=[]
DealerHand=[]

print("Would you like to play BlackJack?")
Q1=input()
print("How many Decks would you like to play with?")
DS=int(input())
while choice == 0:
	if not type(DS) is int:
		print("Please type in a number")
		DS=int(input())
	else:
		choice=0

Full_Deck=MKShoe(DS)
Full_Deck=ShuffleShoe(Full_Deck)

if ("N" in Q1 or "n" in Q1):
	print("Come Back Soon!")
else:
	StartGame(Full_Deck)
