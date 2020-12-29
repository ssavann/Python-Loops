#Create a password generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

"""
#Option 1
password = ""       #generate a password into a string -> less secure

for char in range(1, nr_letters + 1):       
# to include 26 letters, add "+1", otherwise 25 letters only
    random_char = random.choice(letters)
    password = password + random_char   #or  password += random_char
    # print(password)


for char in range(1, nr_symbols + 1):       
    password += random.choice(symbols)   
    # print(password)


for char in range(1, nr_numbers + 1):       
    password += random.choice(numbers)
    # print(password)


print(password)
"""


#option 2
password_list = []       #generate a password in a list. Not a random position.

for char in range(1, nr_letters + 1):       
    password_list.append(random.choice(letters))
    


for char in range(1, nr_symbols + 1):       
    password_list += random.choice(symbols)   
    


for char in range(1, nr_numbers + 1):       
    password_list += random.choice(numbers)


print(password_list)                #will output: Letters + Symbols + Numbers

random.shuffle(password_list)       #will shuffle everything in any position
print(password_list)
 


password = ""   
for char in password_list:
    password += char

print(f"Your password is {password}")