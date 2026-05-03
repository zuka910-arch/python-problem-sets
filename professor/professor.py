import random
def get_level():
    while True:
        try:
            level = int(input("level: "))
            if  level <= 0 or level > 3:
                print("pls enter right level")
            else:
                return level

        except ValueError:
            print("EEE")
            continue


def generate_integer(level):
    if level == 1:
        number = random.randint(0,9)
        return number
    elif level == 2:
        number = random.randint(10,99)
        return number
    elif level == 3:
        number = random.randint(100,999)
        return number
    else:
        print("+++++++")



def main():
   level = get_level()
   score = 0
   for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0
        while tries <3 :
            try:
                answer = int(input(F"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("pls enter a number")
                tries += 1
                continue
        if tries == 3 :
            print(f"{x} + {y} = {x + y}")
   print(f"your score is {score}")


     
if __name__ == "__main__":
    main()