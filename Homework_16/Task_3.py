import random
random_number = 0
random_list = []
for i in range(50):
    random_number = random.randint(1, 30)
    random_list.append(random_number)
    index = random_list[i]
print("list: ", random_list)

# append only non repeated number
new_list = []
for i in random_list:
    if i not in new_list:
        new_list.append(i)
    continue
print("New list: ", new_list)
print("length: ", len(new_list))



