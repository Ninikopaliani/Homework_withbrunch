import random

random_list = []
even_odd_number = dict(even=0, odd=0)

for i in range(100):
    random_list.append(random.randint(1, 100))

for j in range(len(random_list)):
    if random_list[j] % 2 == 0:
        even_odd_number["even"] += 1
    else:
        even_odd_number["odd"] += 1


print(even_odd_number)
