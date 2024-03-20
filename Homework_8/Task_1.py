# პროგრამამ უნდა მოგვთხოვოს სტრიქონის შეყვანა.
# დაბეჭდოს შეყვანილი სტრიქონის ყველა ლუწი ინდექსის მქონე სიმბოლო, გარდა "e"- სიმბოლოსი.

user_input = input("please  enter text: ")
new_word = ""

for i in range(len(user_input)):
    if i % 2 == 0:
        if user_input[i] != "e":
            new_word = new_word+user_input[i]
print(f"new word is: {new_word}", end="")


