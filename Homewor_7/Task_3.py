# დაწერეთ პროგრამა რომელიც მიიღებს არაუარყოფით მთელ რიცხვს -n . 0<=n<10000
# და დაბეჭდავს ამ რიცხვის შებრუნებულ მნიშვნელობას და ამ რიცხვში შემავალი ციფრების ჯამს
# მაგალითი:
# enter number: 7923
# reversed number is 3297
# sum of digits: 21

num = int(input("enter number between [0,10000): "))

if 0 <= num < 10000:
    rev_num = 0
    result = ""
    _sum = 0
    while num != 0:
        rev_num = int(num % 10)
        num = int((num-rev_num)/10)
        result = result+str(rev_num)
        _sum = _sum + rev_num
        continue
    print("reversed number is: ", result)
    print("sum of digits: ", _sum)


else:
    print("please enter valid number")

# ვიცი "else" "while"-სთან არ არის კარგი რომ გამოვიყენოთ მაგრამ ელსის გარეშე  ყველა შემთხევვაში უწერს ამ პრინტს
# და  ამიტომ გამოვიდა ასე :(

