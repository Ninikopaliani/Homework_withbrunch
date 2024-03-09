n = int(input("Enter number from 0 to 50: "))

if 0 < n < 50:
    for i in range(1, n):
        for j in range(1, n):
            if i % j == 0:
                print(round(i/j), " ", end=" ")
        print(i)

else:
    print("please enter valid number")
