def passwordGenerator():
    import string
    import random
    
    paraList = []
    password = []
    count = 0
    
    passLen = int(input("Please enter a number for password length: "))
    while True:
        parameters = int(input("Please select one: 1 for UPPERCASE, 2 for LOWERCASE, 3 for NUMBERS, 4 for SPECIAL CHARACTERS, then press 0 to RUN: "))
        if (parameters == 0) and count >= 1:
            break
        elif (parameters == 1):
            paraList += string.ascii_uppercase
            count += 1
        elif (parameters == 2):
            paraList += string.ascii_lowercase
            count += 1
        elif (parameters == 3):
            paraList += string.digits
            count += 1
        elif (parameters == 4):
            paraList += string.punctuation
            count += 1
        else:
            print("Please choose from an option from above")

    for i in range(passLen):
        randomPara = random.choice(paraList)
        password.append(randomPara)

    print("Your random password generated is: ", str("".join(password)))
passwordGenerator()


