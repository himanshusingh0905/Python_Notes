import random 
import array 

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
		'*', '(', ')', '<'] 


# Logic
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# EASY LEVEL
# Expected_Output: ApbC@#56
# Means Type of characters are together

# password = ""
# for i in range(nr_letters):
# 	password += (random.choice(letters))

# for i in range(nr_numbers):
# 	password += (random.choice(DIGITS))

# for i in range(nr_symbols):
# 	password += (random.choice(SYMBOLS))

# print(password)


#-----------------------------------------------------------------
# Hard level :
# 1. create a list
# 2. append characters 
# 3. shuffle them
# 4. convert into string

password_list = []
for i in range(nr_letters):
	password_list.append(random.choice(letters))
for i in range(nr_numbers):
	password_list.append(random.choice(DIGITS))

for i in range(nr_symbols):
	password_list.append(random.choice(SYMBOLS))

print(password_list)
# shuffling
random.shuffle(password_list)

password = ""
for char in password_list:
	password += char

print(password)