
DB_PASSWORD = "Georgia"
MAX_TRIES = 3

input_password = input("Enter your password: ")

if input_password != DB_PASSWORD:
    for i in range(1, MAX_TRIES):
        if input_password == DB_PASSWORD:
            print("Hello from Georgia")
            break
        input_password = input("please enter correct password: ")
        if i == MAX_TRIES-1:
            if input_password == DB_PASSWORD:
                print("Hello from Georgia")
            else:
                print("you are blocked")


else:
    print("hello from Georgia")


