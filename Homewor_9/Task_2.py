# 2. დაწერეთ პროგრამა რომელიც მიიღებს ორ სტიქონს.
# Პროგრამამ უნდა შეამოწმოს არის თუ არა შესაძლებელი ერთი სტრიქოქნის სიმბოლოების გამოყენებით მეორე სტრიქონის მიღება.
# მაგალითი 1.
# Input:
# listen
# silent
# Output: YES
#
# მაგალითი 2.
# Input:
# a gentleman
# elegant man
# Output: YES
#
# მაგალითი 3.
# Input:
# dormitory
# dirty room
# Output: NO
#
# მაგალითი 4.
# Input:
# election
# collection
# Output: NO

print("input: ")
par_1 = input()
par_1 = par_1.lower()
par_2 = input()
par_2.lower()
k = 0
f = 0

for c in range(len(par_1)):
    if par_1[c] in par_2 and len(par_1) == len(par_2):
        k += 1
        if k == len(par_1):
            pass
    else:
        print("Output: NO")
        break

for s in range(len(par_2)):
    if par_2[s] in par_1 and len(par_1) == len(par_2):
        f += 1
        if f == len(par_2):
            print("Output: YES")
    else:
        print("Output: NO")
        break

