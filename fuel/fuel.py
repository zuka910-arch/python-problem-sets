while True:
    try:
        fuel= input("fraction: ")
        x_str , y_str = fuel.split("/")
        x = int(x_str)
        y = int(y_str)
        if x > y or x < 0 or y < 0:
            continue
        
        percentage = round((x / y) * 100)


        if percentage >= 99:
            print("F")
            break
        elif percentage <= 1:
            print("E")
            break
        else:
            print(f"{percentage}%")
            break

    except ValueError:
        continue
    except ZeroDivisionError:
        continue