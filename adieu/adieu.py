import inflect
p = inflect.engine()
name_list = []
while True:
    try:
        input_name= input(" ")
        name_list.append(input_name)
        new_name_list = p.join(name_list)
    except EOFError:
        print(f"Adieu, adieu, to {new_name_list}")
        break
