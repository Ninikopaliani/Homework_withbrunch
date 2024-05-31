import random


def sum_number():
    list_1 = []
    list_2 = []
    list_3 = []
    for i in range(1, 10):
        random_number_1 = random.randint(1, 10)
        random_number_2 = random.randint(1, 10)
        random_number_3 = random.randint(1, 10)
        list_1.append(random_number_1)
        list_2.append(random_number_2)
        list_3.append(random_number_3)
    print(list_1, list_2, list_3)

    sum_numbers = []
    for x in map(lambda a, b, c: a + b + c, list_1, list_2, list_3):
        sum_numbers.append(x)
    print("Sum of the number is: ", sum_numbers, end=" ")


sum_number()