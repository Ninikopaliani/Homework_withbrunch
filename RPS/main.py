import random


def play_round():
    choices = ['r', 'p', 's']
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice r, p, s: ").upper()

    if computer_choice == user_choice:
        print(" It's a draw!")
        return 0, 0
    elif (computer_choice == 'r' and user_choice == 's') or \
            (computer_choice == 's' and user_choice == 'p') or \
            (computer_choice == 'p' and user_choice == 'r'):
        print(f"Computer - {computer_choice} and you - {user_choice}. Computer wins this round!")
        return 1, 0
    else:
        print(f"Computer- {computer_choice} and you - {user_choice}. You win this round!")
        return 0, 1


def play_game():
    user_score = 0
    computer_score = 0

    while user_score < 3 and computer_score < 3:
        round_result = play_round()
        computer_score += round_result[0]
        user_score += round_result[1]
        print(f"You: {user_score}, Computer: {computer_score}\n")

    if user_score == 3:
        print("winner is user")
    else:
        print("winner is computer")


play_game()












