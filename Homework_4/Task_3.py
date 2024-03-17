
divider = int(input("Enter number: "))

if divider > 0:
    for i in range(1, divider+1):
        if divider % i ==0:
            print(round(divider/i), end=" ")

else :
    print("please enter valid number")


