#random ah import panrom 
from random import randint

#rock paper and scissor ah ellam oru list la podrom

t = ["rock" , "paper", "scissor"]

#computer random ah choose pananum athuku namma atha ippa assign panna porom

computer = t[randint(0,2)]

"""Ippa namma assign panitom
--> computer ethuku na athu oru variable --> t ethuku potu irukom na namma munnadi rock paper siccor 3 ya um list la add pannom, athuku variable name t nu vechom la athan -->t nu potu irukom
--> randit ethuku potu irukom na atha vechu tha namma random ah computer ah decisions eduka veika porom, atha namma munnadiye import pani irukom mela paarunga #2nd line la
--> 0,2 ethuku potu irukom na,
namma motham 3 values assign pani irukom:
	1st --> rock : atha namma 0 nu vechukalam
	2nd --> paper : atha  namma 1 nu vechukalam
	3rd --> scissor : atha namma 2 nj vechukalam
so athunaala than namma --> 0,2 type pani irukom
"""
#ippa namma player = False nu potu irukom athu en na, while loop ah paarunga ungaluke purium. Ellathaum naney solikitu iruntha nalla irukaathu
player = False

while player == False:

#ippa namma player ah true ah set panna porom
	print("")
	print("Type the object that you want to choose")
	player = input("rock, paper, scissor:")
	if player == computer:
		print("Both of them are choosen same objects <•_• > So The Result is Tie!")
	elif player == "rock":
		if	computer == "paper":
			print("You Losed Bruh <•_•> The Computer wins!")
		else:
			print("You Win Bruh! You Smashed The Computer!")
	elif player == "paper":
		if computer == "scissor":
				print("You Losed Bruh <•_•> The Computer wins!")
		else:
				print("You Win Bruh! You Smashed The Computer!")
	elif player == "scissor":
		if computer == "rock":
				print("You Losed Bruh <•_•> The Computer wins!")
		else:
				print("You Win Bruh! You Smashed The Computer!")
	else:
				print("Check Your Spelling Bruh!")
		
	player = False
	computer = t[randint(0,2)]
	
#Ithoda program Mudinchu 				
"""namma player value ah true ah set panni irukom ippa namma false  nu mathitom so en ipadi panom na apa tha namku loop continue aagum, namma thodranthu vilada mudiyum. illena namma program end ayirum """					