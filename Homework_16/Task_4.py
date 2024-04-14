import random
random_list_a = []
random_list_b = []
for i in range(5):
    random_list_a.append(random.randint(1, 10))
    random_list_a = sorted(random_list_a)
print("list a:", random_list_a)

for i in range(5):
    random_list_b.append(random.randint(1, 10))
    random_list_b = sorted(random_list_b)
print("list b:", random_list_b)

new_list = []
for i in range(len(random_list_a)):
    if random_list_b[i] > random_list_a[i]:
        new_list.append(random_list_a[i])
        new_list.append(random_list_b[i])
    else:
        new_list.append(random_list_b[i])
        new_list.append(random_list_a[i])
print(new_list)

for c in range(0, len(new_list)):
    for k in range(c+1, len(new_list)):
        if new_list[c] >= new_list[k]:
            new_list[c], new_list[k] = new_list[k], new_list[c]
print("sorted list: ", new_list)


