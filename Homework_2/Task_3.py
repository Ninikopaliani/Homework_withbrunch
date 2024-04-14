number_1 = int(input("შეიყვანე რიცხვი 1-დან 10-ის ჩათვლით: "))
a = number_1 % 2
b = number_1 % 3
c = number_1 % 5
e = number_1 % 7
if number_1 <= 10:
    if a == 0 and b == 0:
        print(number_1//2, ",", number_1//3)
    elif a == 0 and c == 0:
        print(2, ",", 5)
    elif a == 0 and e == 0:
        print(2, ",", 7)
    else:
        print("რიცხვს აქვს 2ზე ნაკლები მარტივი გამყოფი , გარდა თავის თავისა და 1-ის")
else:
    print("გთხოვთ შეიყვანეთ, 1-დან 10-ის ჩათვლით რიცხვი")
