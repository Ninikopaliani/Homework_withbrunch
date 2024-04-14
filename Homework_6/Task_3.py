import random
DB_PASSWORD = random.randint(1, 100)
MAX_TRIES = 10

input_password = int(input("Please enter number: "))

tries = 1
while DB_PASSWORD != input_password:
    if tries == MAX_TRIES:
        print("Computer is winner")
        break
    tries += 1
    if input_password > DB_PASSWORD:
        print("high")
    elif input_password < DB_PASSWORD:
        print("low")
    input_password = int(input("Number was not correct. Try again - "))

if DB_PASSWORD == input_password:
    print("You are  winner ")

