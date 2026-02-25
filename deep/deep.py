def main():
    answer = input("what is the Answer to the Great Question of life, the Universe, and Everything?").lower().strip()

    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("yes")
    else:
        print("no")



main()
