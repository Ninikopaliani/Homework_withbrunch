n = int(input("Enter number in range  (0 < n < 10): "))

if 0 < n < 10:
    i = 0
    while i < n:
        j = 0
        while j < n - i:
            print("   ", end="")
            j += 1
        j = i
        while j >= 0:
            print(f" {j} ", end="")
            j -= 1
        j = 1
        while j <= i:
            print(f" {j} ", end="")
            j += 1

        print()
        i += 1
else:
    print("please enter valid number")

