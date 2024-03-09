
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))


for i in range(a):
    for j in range(b):
        if i == 0:
            if j != b//2:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        elif 0<i<(a-1):
            if j < b//2:
                print("/" , end=" ")
            elif j==b//2:
                print("|",end=" ")
            elif j > b//2:
                print("/", end=" ")

# ვერ ჩავწერე ასეთიჩანაწერი -  \"

        elif i== a-1:
            if j != b//2:
                print(" " ,end=" ")
            else:
                print("|", end=" ")
    print()