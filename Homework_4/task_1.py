import random

def rolldice():
    return random.randint(1, 6)
player = int(input("enter the number of players: "))

if player < 1:
    print("please enter valid value")
for i in range(player):
    dice_1 = rolldice()
    dice_2 = rolldice()
    print(dice_1, dice_2)


