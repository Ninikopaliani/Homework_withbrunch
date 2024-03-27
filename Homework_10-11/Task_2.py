import random
import math
n = int(input("please enter number: "))
counter = 0
for i in range(n):
    a = random.random()
    b = random.random()
    if math.sqrt(a**2+b**2) <= 1:
        counter += 1
# print(a, b)
print(4*counter/n)


