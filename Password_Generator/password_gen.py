import random as r

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['0','1','2','3','4','5','6','7','8','9']
special_characters = ['!','#','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']

print("Welcome to the PyPassword Generator!")
nr_small_letter = int(input("How many small letters would you like in your password?\n"))
nr_capital_letters = int(input("How many capital letters would you like in your password?\n"))
nr_number = int(input("How many numbers would you like in your password?\n")) 
nr_special_characters = int(input("How many special characters would you like in your password?\n"))


password = []

for i in range(nr_small_letter):
    password.append(r.choice(letters))

for i in range(nr_capital_letters):
    password.append(r.choice(capital_letters))

for i in range(nr_number):
    password.append(r.choice(number))

for i in range(nr_special_characters):
    password.append(r.choice(special_characters))

r.shuffle(password)
password = "".join(password)
print(password)