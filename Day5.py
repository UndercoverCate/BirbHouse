# fruits = ["apple" , "peach", "grape" , "orange"]
# for stink in fruits:
#     print(stink)
#     print (stink + "ew")

# student_scores = [180,124,165,173,189,169,146]
# total_scores = sum(student_scores)
# print(total_scores)

# student_scores = [180,124,165]
# sum = 0
# for score in student_scores:
#         sum += score
# print (sum)

# max_score = 0
# student_scores = [8,65,89,86,55,91,64,89]
# for score in (student_scores):
#     if score > max_score:
#         max_score=score
#         print (max_score)


#1-100
#if /3 it will print "fizz"
#if /5 it will print "buzz"
# if / by both /3 and /5 itll print "fizzbuzz"
#otherwise just print the remaing list


# for number_list in range(1,101):
#     if number_list %3==0 and number_list %5== 0:
#         print ("fizzbuzz")
#     elif number_list %3 == 0 :
#         print ("fizz")
#     elif number_list %5==0:
#         print("buzz")
#     else: print (number_list)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_letter_pool=[]
random_symbol_pool=[]
random_number_pool=[]
password=[]
random_password=[]
#ez
for step_one in range(nr_letters):
     step_one = random.choice(letters)
     random_letter_pool.append(step_one)
#print(random_letter_pool)

for step_two in range(nr_symbols):
     step_two = random.choice(symbols)
     random_symbol_pool.append(step_two)
#print(random_symbol_pool)

for step_three in range(nr_numbers):
     step_three = random.choice(numbers)
     random_number_pool.append(step_three)
#print(random_number_pool)

password.append(random_letter_pool)
password.append(random_symbol_pool)
password.append(random_number_pool)

