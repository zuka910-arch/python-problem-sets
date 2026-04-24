import random

while True:
    try:
        level = int(input("level: "))
        if level > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("pls enter number")
        continue
secret_number = random.randint(1, level)

while True:
    try:
        guess = int(input("guess: "))
        if guess <= 0:
             continue
                
        if guess < secret_number:
                print("Too small!")
        elif guess > secret_number:
                print("Too large!")
        else:
                print("Just right!")
                break
            
    except ValueError:
        print("pls enter number")
        continue
