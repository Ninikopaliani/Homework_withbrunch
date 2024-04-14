import random
random_number = 0
random_list = []
for i in range(5):
    random_number = random.randint(1, 5)
    random_list.append(random_number)
    index = random_list[i]
print("list: ", random_list)


# Repeat each list member as many times as the number of digits in random_list


def long_list():
    random_long_list = []
    for k in random_list:
        for c in range(k):
            random_long_list.append(k)
    print("New list: ", random_long_list)
    print("Length: ", len(random_long_list))


long_list()




