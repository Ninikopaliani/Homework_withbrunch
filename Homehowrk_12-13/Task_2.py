a = input("Input a: ")
b = input("Input b: ")
for c in a:
    k = a[len(a)-1]
    a = k+a
    a = a[0:len(a)-1]
    if a == b:
        break
    pass

if a == b:
    print("Output: yes")
else:
    print("Output: No")













