n = int(input("please enter number (0-10): "))

if 0 < n < 10:
    i = 1
    while i < (n+1) * 2:
        j = 1
        if i <= n+1:
            while j <= i-1:
                print(f"{j}", end=" ")
                j += 1
        else:
            while j < 2 * (n+1) - i:
                print(f"{j}", end=" ")
                j += 1
        print()
        i += 1
else:
    print("please enter valid number")
