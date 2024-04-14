n = int(input("Enter tree size: "))
# pint n-i" " და i"*"
for i in range(n):
    if i == 0:
        top = (" " * (n - i)) + ((i+1) * "*")
        print(top)
    elif 0 < i < (n-1):
        middle = ((" " * (n - i)) + (i * "/") + "|" + (i * '\\'))
        print(middle)
    elif i == (n-1):
        bottom = (" " * n + "|")
        print(bottom)
