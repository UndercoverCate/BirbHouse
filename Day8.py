# # def greet():
# #     print ("hello")
# #     print ("welcome")
# #     print ("K bai")

# # player = input ("Please type hello ").lower()

# # if player == "hello":
# #     greet()

# # greet with name
# name1 = input("What is your name? ")
# location = input ("Where are you from")

# def greet_with_name(name,location):
#     print (f"Hello{name}.")
#     print (f"How are you {name}?")
#     print (f"Oh you are from {location}? how is it there?")

# greet_with_name(name1 ,location)

# # age = int(input("How old are you? "))

# # def life_in_weeks(age):
# #     weeks_left = (90 - age) *52
# #     print (f"you have {weeks_left} weeks left")

# # life_in_weeks(age)



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode to encrypt or 'decode' to decrypt\n").lower()
shift = int(input("type the shift number:\n"))

# Todo-1: Create a function called 'encrypt()' that takes the original_text and shift_amount as 2 inputs
encrypt = []
final_encrypt=""

original_text = input("Please type a word for encryption:\n")
for letters in original_text:
    encrypt = [alphabet.index(letters) + shift]
print (encrypt)
    
    # for numbers in encrypt:
    #     final_encrypt = alphabet.index(numbers)
    # print (final_encrypt)


# Todo-2: Inside the 'encrpyt()' function, shift each letter of the 'original_text' by the 'shift_amount' and print the encrypted text.

# Todo-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# Todo-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test code and encrypt it.
  