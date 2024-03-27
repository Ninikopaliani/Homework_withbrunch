n = int(input("please enter number: "))
s = 0
for i in range(1, n):
    s = 1/(2*i-1)
    if i % 2 == 0:
        s = -s
    else:
        s = s
    s += s
print(4*s)





