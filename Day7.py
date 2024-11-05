# #Randomly choose a word from word list and save it as a variable called "chosen_word". Then print it.
import random

# word_list = ["aardvark" , "baboon" , "camel"]
# chosen_word= random.choice(word_list)
# print (chosen_word)

# #blanks to guess off of
# place_holder = ""
# for position in range(1,len(chosen_word)):
#     place_holder += ("_ ")
# print (place_holder)



# # #gameplay loop

# #players input

# correct_letters = []
# #loop

# lives = 6
# gameover = False
# while not gameover:
#     display = ''
    
#     print(lives)
#     players_guess = input("Hangman, guess a letter: ").lower()
#     for letters in chosen_word:
        
#         if letters == players_guess:
#             display += letters
#         else:display += ("_ ")

#         if letters != players_guess:
#             lives -1
            

#     print (display)
# print (lives)
# if "_" not in display:
#     gameover = True
#     print("you win")
# if lives == 0:
#     gameover = True
#     print ("you lose")


#--------------------------------------------------------------------- krys redo--------------------------------------
# word_list = ["aardvark" , "baboon" , "camel"]
# #select word to guess
# chosen_word= random.choice(word_list)
# print (chosen_word)

# #create starting display
# display = ""
# for chosen_word_letters in chosen_word:
#     display += "_ "
# #print (display)


# #setup Variables ex: lives, correct letters list
# lives = (6)
# correct_letters = []

# #setup gameplay loop
# game_over = False
# while game_over == False:
#     loop_display=""

#     #ask user question
#     players_guess = input(f"{display}\nHangman, please guess a letter: ")
#     for letters in chosen_word:

#         #if correct add to correct letter list
#         if players_guess == letters:
#             loop_display += players_guess
#             correct_letters.append(players_guess)

#         #if incorrect, remove a life   
        
#         print (loop_display)
#         print (lives)
#     if correct_letters is len(chosen_word):
#         game_over == True
#         print ("you win")

# #print updated display using a loop , if else statement.



#---------------------------------Angela--------------------------
#word list
word_list = ["aardvark" , "baboon" , "camel"]
chosen_word = random.choice(word_list)
print (chosen_word)

#blank generation
place_holder = ""
for position in range(1,len(chosen_word)):
    place_holder += ("_ ")
print (place_holder)

#counters
lives = 6
correct_letters = []
game_over = False

#gameplay loop
while game_over is False:
    display = ""
    guess = input("guess a letter: ").lower()
    print (f"\nYou have {lives} left.")

    #if guess is correct
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else: display += "_ "

    #if guess is incorrect/lose
    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            game_over = True
            print ("you died")
    
    #if you win
    if "_ " not in display:
        game_over = True
        print("you win")
    
    print (display)