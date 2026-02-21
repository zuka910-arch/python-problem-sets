def main():
    users_emoji = input()
    result = convert(users_emoji)
    print(result)


def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")

    return(text)


main()