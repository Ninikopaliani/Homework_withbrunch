import random

n = int(input("enter number: "))

generate_number = [random.randint(0, 1000) for i in range(n)]
print(generate_number, "--- max is: ", max(generate_number))
