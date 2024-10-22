#user_number = (int(input("Input a number: ")))
#odd_even = (user_number % 2)
#if (odd_even == 0) :
#    print ("your number is even.")
#else: print ("you number is odd.")

#weight = 85
#height = 1.85
#bmi = weight / (height ** 2)

#if bmi >= 25 :
#   print("overweight")
#elif bmi <=18.5 :
#   print("normal weight")
#elif bmi <18.5:
#   print("underweight")



#Small pizza 15
#medium pizza 20
#large pizza 25
#add pep 2
#add cheese 1

# print ("Welcome to Python Pizza Deliveries!")
# size = input("what size pizza would you like? S, M, or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M" :
#     bill += 20
# elif size == "L" :
#     bill += 25
  
# if pepperoni == "Y" :
#     if size == "S" :
#         bill += 2
#     else: bill += 3
# if extra_cheese == "Y":
#         bill += 1
# print(f"Your total pizza cost is ${bill}.")

# print ("welcome to the rollercoaster")
# height = int(input("what is your height?"))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age?"))
#     if age >= 45 and age <= 55:
#         bill = 0
#         if age < 12:
#             bill += 5
#             print("child tickets are 5$")
#         elif age <= 18:
#             bill += 7
#             print("youth tickets are 7")
#     else:
#         bill = 12
#         print("adult tickets are 12")

#     wants_photo = input("Do you want a photo for $3 Y/N?")
#     if wants_photo == "Y":
#         bill += 3
#     print (f"your total comes out to {bill}.")
# else:
#     print("sorry you are too short to ride")



print(''' 
   /\                                                        /.
  |  |                                                      |  |
 /----\                                                    /----
[______]                                                  [______]
 |    |         _____                        _____         |    |
 |[]  |        [     ]                      [     ]        |  []|
 |    |       [_______][ ][ ][ ][][ ][ ][ ][_______]       |    |
 |    [ ][ ][ ]|     |  ,----------------,  |     |[ ][ ][ ]    |
 |             |     |/'    ____..____    '\|     |             |
  \  []        |     |    /'    ||    '\    |     |        []  /
   |      []   |     |   |o     ||     o|   |     |  []       |
   |           |  _  |   |     _||_     |   |  _  |           |
   |   []      | (_) |   |    (_||_)    |   | (_) |       []  |
   |           |     |   |     (||)     |   |     |           |
   |           |     |   |      ||      |   |     |           |
 /''           |     |   |o     ||     o|   |     |           ''.
[_____________[_______]--'------''------'--[_______]_____________]''')

Choice1=input("welcome to treasure castle, your goal is to find the hidden treasure, and probably not die.\nWhich path will thou taketh?\nFront door or Around back? ")
if Choice1 == "Around back" or Choice1== "around back" or Choice1=="Around Back" or Choice1=="around Back" :
    Choice2=input("You have succesfully avoided the guards in the front of the castle.\n\nYou can now go to two paths; Servants Quarters or Throne Room? ")
    if Choice2 == "Servants Quarters" or Choice2 == "servants quarters" or Choice2 == "Servants quarters" or Choice2 == "servants Quarters":
      
        Choice3 =input("Very clever to blend in with the servants, you managed to sneak into the royal loft..\n\n You now have three doors presented which one shall you enter? Gold, Iron, or Blue? ")
        if Choice3 == "Gold" or Choice3 == "gold":
            print('''You found the treasure in kings room, better make fast and escape! ''')
        elif Choice3 == "Iron" or Choice3 == "iron":
            print("Well, you just walked yourself into the dungeon..\n Congrats..? You did the guards job. ")
      
        else: print('''
        | \        /|
        |  \____  / |
       /|__/AMMA\/  |
     /AMMMMMMMMMMM\_|
 ___/AMMMMMMMMMMMMMMA
 \   |MVKMMM/ .\MMMMM
  \__/MMMMMM\  /MMMMMM---
  |MMMMMMMMMMMMMMMMMM|  /
  |MMMM/. \MM.--MMMMMM\/
  /\MMM\  /MM\  |MMMMMM   ___
 /  |MMMMMMMMM\ |MMMMMM--/   \-.
/___/MMMMMMMMMM\|M.--M/___/_|    |
     \VMM/\MMMMMMM\  |      /\ \/
      \V/  \MMMMMMM\ |     /_  /
        |  /MMMV'   \|    |/ _/
        | /              _/  /
        |/              /|   /
                       /_  /
                       /  / 
                       The blue door lead into the armoury, good luck fighting the guards..\n You died''') 
    else:print("A bold attempt going into the throne room without a disguise.. the royal guard has captured you.. Try again.")
else:print ("Wow, you expected to NOT get shot at the gate, you are dead.")
