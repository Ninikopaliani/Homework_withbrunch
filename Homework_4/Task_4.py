a, b = 0, 1
n = int(input("Enter number: "))


if 0 < n <= 20:
    for i in range(n):
        a, b = b, a + b
        print(a)
else:
    print("Enter valid number please")

