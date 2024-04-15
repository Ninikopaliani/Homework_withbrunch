import random


def random_():
    digit = "rps"
    random_number = random.randint(1, 3)
    random_digit = digit[random_number]
    return random_digit


def user():
    user_digit = input("please enter digit (r,p,s): ")
    return user_digit


def main():
    if random_() == user():
        print("ფრე")
    else:
        if random_() == "s" and user() == "r":
            print("winner user")
        elif random_() == "r" and user() == "s":
            print("winner computer")
        elif random_() == "s" and user() == "p":
            print("winner computer")
        elif random_() == "p" and user() == "s":
            print("winner user")
        elif random_() == "p" and user() == "r":
            print("winner computer")
        elif random_() == "r" and user() == "p":
            print("winner user")


main()



