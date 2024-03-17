A = int(input("please, input number A : "))
B = int(input("please, input number B : "))
N = A % B
if N == 0:
    print("A რიცხვს ეწოდება B რიცხვის ჯერადი")
else:
    print("A რიცხვი უნაშთოდ არ იყოფა B-ზე, B რიცხვი A-ში მოთავსდება", A//B, "-ჯერ, ნაშთია-", A % B)
