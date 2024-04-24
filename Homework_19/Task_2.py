string_text = input("please enter text: ")

string_dict = {}

for i in range(len(string_text)):
    string_dict[string_text[i]] = string_text.count(string_text[i])

print(string_dict)