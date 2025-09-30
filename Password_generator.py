import string
import random

password_length = int(input("How many characters is your password? "))

print('''Choose character set for password from these : 
         1. Numbers
         2. Letters
         3. Special characters
         4. Exit''')

characterList = ""

while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
        characterList = characterList + string.digits
    elif(choice == 2):
        characterList = characterList + string.ascii_letters
    elif(choice == 3):
        characterList = characterList + string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a number from 1 to 4")

password = []


for i in range(password_length):
    randomcharacter = random.choice(characterList)
    password.append(randomcharacter)


print("Your password is: " + "".join(password))