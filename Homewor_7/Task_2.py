# დაწერეთ პროგრამა რომელიც მიიღებს დადებით მთელ რიცხვს-n. 0<n<=1000,
# პროგრამამ უნდა დაბეჭდოს რიცხვების მიმდევრობა რომელიც მიიღება შემდეგი პირობით:
# თუ რიცხვი ლუწია, ეს რიცხვი უნდა გავყოთ 2-ზე, ხოლო თუ რიცხვი კენტია ეს რიცხვი გავამრავლოთ 3-ზე და დავუმატოთ 1
# მაგ:
# enter number: 10
# 10->5->16->8->4->2->1

n = int(input("enter number between 0 and 1000: "))

# check if the number is valid
if 0 < n <= 1000:
    j = 0
    i = n  # variable for iterator
    print(n, end="")
    while i > 1:
        k = i % 2
        if k == 0:
            j = i/2
            i = int(j)
            print("->", i, end="")  # if this condition is working
            continue  # if this condition does not work, continue
        j = i*3+1
        i = int(j)
        print("->", i, end="")
        continue
    i -= 1
else:
    print("please enter valid number")

