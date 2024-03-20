# პროგრამამ უნდა შეგვაყვანინოს სიტყვა და დაბეჭდოს ამ სიტყვიდან მხოლოდ თანხმოვანი ასოები.

text_input = input("please input text: ")
consonant = ""

for c in text_input:
    if c != "a" and c != "e" and c != "i" and c != "o" and c != "u":
        consonant = consonant+c
print(f"new word is: {consonant}", end="")