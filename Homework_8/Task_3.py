# პროგრამამ შეგვაყვანინოს სიტყვა და დაბეჭდოს ბოლო, პირველი და შუა ასოები 5-ჯერ while ლუპით.
# თუ შემოყვანილი ტექსტის ზომა არის ლუწი, მაშინ პროგრამამ უნდა დაბეჭდოს შუა ორი სიმბოლო.

text_input = input("please enter text: ")
_len = len(text_input)
middle = int(len(text_input)/2)
last = int(len(text_input))-1
median = middle+1
c = 0
n = 5
if _len % 2 != 0:
    while c < n:
        print(text_input[last]+text_input[0]+text_input[middle], " ", end="")
        c += 1
else:
    print(text_input[middle-1]+text_input[median-1])
