message = input("camelCase: ")

for letter in message:
    if letter.isupper():
        message = message.replace(letter, "_" + letter.lower())



print(message)

    
