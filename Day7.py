#Randomly choose a word from word list and save it as a variable called "chosen_word". Then print it.
import random



word_list = ["aardvark" , "baboon" , "camel"]
chosen_word= random.choice(word_list)
print (chosen_word)


placeholder= ""
for blanks in chosen_word:
    placeholder += "_ "
print (placeholder) 

guess=''
display = ""
while (display) is not (chosen_word):
    guess = input("Guess the letter of the word: ").lower()
    for letters in chosen_word:
        if letters == guess:
            display += (guess)
        else: print ("try again")
    print(display)
print("you win")



