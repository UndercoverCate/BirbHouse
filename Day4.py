import random

#random_integer = random.randint (1 , 10)
#print (random_integer)

# random_number = random.random()
# print (random_number)

# random_float = random.uniform(1 , 10)
# print (random_float)

# input("Heads or Tails? " )
# coinflip = random.randint (1,0)
# if coinflip == 0 :
#     print ("\nHeads")
# else: print ("\nTails")

# friends = ['Alice' , "Bob" , "Charlie" , "David" , "Emanuel"]
# print(random.choices(friends))

# Dirt_dozen = ["Strawberries" , "Spinach" , "Kale" , "Nectarines" , "Apples" , "Grapes" , "Peaches" "Pears"]


# rock = ("A cool picture of a rock")
# paper = ("A cool picture of some paper")
# scissors = ("A cool picture of some scissors")


# RPS = [rock , paper , scissors]
# player_choices = []

# player = input("Rock paper scissors.\n Choose 1 for Rock, 2 for Paper, or 3 for scissors " )
# if player == "1" : player_choices.append ("prock")
# elif player == "2" : player_choices.append ("ppaper")
# else: player_choices.append ("pscissors")
    
# print (player_choices)

# # print (random.choices(RPS))
# if (random.choices(RPS)) == player_choices:
#     print ("Tie")
#     if (random.choices(RPS)) == "rock" and player_choices == "['ppaper']" : 
#         print ("you win")



        
#dealers options
rock = ("rock")
paper = ("paper")
scissors = ("scissors")
dealer = [rock , paper , scissors]

#dealers hand + players hand
dealers_hand = random.choices(dealer)
players_hand = []

#players input
players_choice = input("Rock, paper, scissors.\nType 1 for Rock, 2 for Paper, and 3 for Scissors:\n")
if "1" in players_choice:
   players_hand.append (rock)
if "2" in players_choice:
    players_hand.append (paper)
if "3" in players_choice:
    players_hand.append (scissors)

#if tie
    print("missing input")
if dealers_hand == players_hand :
    print (f"dealer chose {dealers_hand} you Tie")

#if rock
elif "rock" in dealers_hand:
    if "paper" in players_hand:
     print ("dealer chose rock you win")
    else: print ("dealer chose rock you lose")

#if paper
elif "paper" in dealers_hand:
    if "scissors" in players_hand:
     print ("dealer chose scissor you win")
    else: print ("dealer chose scissor you lose")

#if scissors
elif "scissors" in dealers_hand:
    if "rock" in players_hand:
     print ("dealer chose scissors you win")
    else: print ("dealer chose scissors you lose")