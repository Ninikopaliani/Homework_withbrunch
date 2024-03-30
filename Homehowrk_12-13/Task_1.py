name = input("Input: ")
print("Output: ")
for c in name:
    k = name[len(name)-1]
    name = k+name
    name = name[0:len(name)-1]
    print(name)

