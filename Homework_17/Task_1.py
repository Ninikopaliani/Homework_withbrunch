import random


def min_func(rand_list):
    return min(rand_list)


def max_func(rand_list):
    return max(rand_list)


def sorted_func(rand_list):
    rand_list = sorted(rand_list)
    return rand_list


# def apply_to_each(elements, func):
#     for i in range(len(elements)):
#         elements[i] = func(elements[i])


def main():
    list_rand = []
    for i in range(1, 10):
        random_number = random.randint(1, 10)
        list_rand.append(random_number)
    print("Random-list: ", list_rand)
    print("Min number from list: ", min_func(list_rand))
    print("Max number from list: ", max_func(list_rand))
    print("Sorted list: ", sorted_func(list_rand))


main()
