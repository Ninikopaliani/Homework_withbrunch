def words():
    list_str = ["I", "have", "to", "write", "some", "words", "like", "this:", "sky", "car", "bag"]
    print("firs list is: ", list_str)

    list_new = []
    for x in filter(lambda item: len(item) <= 3, list_str):
        list_new.append(x)
    print("New list is: ", list_new)


words()

