import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
           'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '_']

print("Welcome to the PyPassword Generator!")
n1 = int(input("How many letters would you like in your password?\n"))
n2 = int(input("How many symbols would you like?\n"))
n3 = int(input("How many numbers would you like?\n"))

 #Easy Level: Printing in order

'''
password = ""

for char in range(1, n1 + 1):
    password += random.choice(letters)

for char in range(1, n2 + 1):
    password += random.choice(symbols)

for char in range(1, n3 + 1):
    password += random.choice(numbers)

print(password)


'''

# Hard Level

password = []

for char in range(1, n1 + 1):
    password.append(random.choice(letters))

for char in range(1, n2 + 1):
    password.append(random.choice(symbols))

for char in range(1, n3 + 1):
    password.append(random.choice(numbers))

#print(password)
random.shuffle(password)
#print(password)

password_generated = ""
for char in password:
    password_generated += char
print(f"Your Generated Password: {password_generated}")




