import string

SYMBOLS = string.ascii_letters + string.punctuation + string.digits + " "

message = input("Please enter message: ")
distance = int(input("Please enter key size: "))
choice = input("Choose Encrypt or Decrypt: ")
code = ""
text = ""

n = len(message)

mode = ['Encrypt','Decrypt']

while True:
    if choice == mode[0]:
        for ch in range(n):
            character = message[ch]
            location = SYMBOLS.find(character)
            new_location = (location + distance) % 127
            code += SYMBOLS[new_location]
        print(code)
        break

    elif choice == mode[1]:
        for ch in range(n):
            character = message[ch]
            location = SYMBOLS.find(character)
            new_location = (location - distance) % 127
            text += SYMBOLS[new_location]
        print(text)
        break
            
        
