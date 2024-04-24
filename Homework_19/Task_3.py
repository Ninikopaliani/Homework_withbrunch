def friends(friendships, friend1, friend2):
    if friend1 not in friendships:
        friendships[friend1] = []
    if friend2 not in friendships:
        friendships[friend2] = []
    friendships[friend1].append(friend2)
    friendships[friend2].append(friend1)


def print_friendships(friendships):
    for person, friends in friendships.items():
        print(f"{person} - {', '.join(friends)}")


def main():
    friendships = {}

    while True:
        info = input("Enter friendship info(or 'FINISH' to end): ").strip()
        info = info.upper()
        if info == "FINISH":
            print("\ninput")
            print_friendships(friendships)
            break

        if " - " in info:
            friend1, friend2 = info.split(" - ")
            friends(friendships, friend1, friend2)
            print(f"{friend1} - {friend2}, {', '.join(friendships[friend1])}")
            print(f"{friend2} - {friend1}, {', '.join(friendships[friend2])}")
        else:
            print("Please enter in the format 'friend1 - friend2'.")


if __name__ == "__main__":
    main()




