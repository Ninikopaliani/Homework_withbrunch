#n = int(input("Enter number from 0 to 50"))1

# n = int(input("Enter tree size: "))
# for i in range(n):
#     line = (" " * (n - i)) + ((i * 2 + 1) * "/")
#     print(line)
#
# t = n // 10
# t = t if t != 0 else 1
# t = t or 1
#
# for i in range(t):
#     line = (" " * (n - t)) + ("#" * t)
#     print(line)


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
                print("[" , end=" ")
            elif j==b//2:
                print("|",end=" ")
            elif j > b//2:
                print("]", end=" ")

# ვერ ჩავწერე ასეთიჩანაწერი -  \"

        elif i== a-1:
            if j != b//2:
                print(" " ,end=" ")
            else:
                print("|", end=" ")
    print()
