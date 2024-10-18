import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list = []
password_str = ""
print("Welcome to PyPassword Generator")
no_letters = int(input("How many letters would you like in your password?\n"))
no_numbers = int(input("How many numbers would you like?\n"))
no_symbols = int(input("How many symbols would you like?\n"))

for letter in range(0, no_letters):
    password_list.append(letters[random.randint(0, len(letters)-1)])

for number in range(0, no_numbers):
    password_list.append(numbers[random.randint(0, len(numbers)-1)])

for symbol in range(0, no_symbols):
    password_list.append(symbols[random.randint(0, len(symbols)-1)])

random.shuffle(password_list)

for word in password_list:
    password_str += ''.join(word)

print(f"Your password can be {password_str}")
