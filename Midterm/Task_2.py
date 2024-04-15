n = int(input("please enter number between [100, 1000): "))
counter = 0
if 100 > n >= 1000:
    print("your number is not correct")
else:
    for i in range(1, n+1):
        if i % 13 == 0:
            print(i)
            counter += 1

        else:
            continue
print(counter)