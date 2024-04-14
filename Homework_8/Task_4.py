# *დაწერეთ პროგრამა რომელიც მომხმარებლის შემოყვანილ ტექსტს
# დაშიფრავს ან განშიფრავს და დაბეჭდავს ეკრანზე.
# დაშიფვრის ლოგიკა ასეთია, ყოველი სიმბოლო უნდა შეიცვალოს კლავიატურაზე მის მარჯვნივ მდგომი სიმბოლოთი.
# Თუ სიმბოლოს მარჯვნივ კლავიატურაზე ინგლისური სიმბოლო არ არის, მაშინ უნდა გადავიდეს პირველ სიმბოლოში ამ სტრიქონიდან.
# Მაგალითად: p -> q, l -> a და ა.შ.
# პროგრამამ უნდა გარდაქმნას მხოლოდ დაბალი რეგისტრის ინგლისური სიმბოლოები a-z.
# Მაგ. 1: Enter action (e/d): e
# Enter text: power qpert
#
# მაგ. 2: Enter action (e/d): d
# Enter text: quyjpm
# python

line_1_symbols = "zxcvbnmasdfghjklqwertyuiop"

action = input("encrypt or decrypt (e/d): ")
if action != "e" and action != "d":
    print("try again")
else:
    text = input("please enter text: ")
    text = text.lower()
    output_text = ""

    if action == "e":
        for c in text:
            for i in range(len(line_1_symbols)):
                if c == line_1_symbols[i] and c != "m" and c != "l" and c != "p":
                    print(line_1_symbols[i+1], end="")
                    pass
                elif c == line_1_symbols[i] and c == "m":
                    print(line_1_symbols[0], end="")
                    pass
                elif c == line_1_symbols[i] and c == "l":
                    print(line_1_symbols[i-8], end="")
                elif c == line_1_symbols[i] and c == "p":
                    print(line_1_symbols[i-9], end="")

        print()
    if action == "d":
        for c in text:
            for i in range(len(line_1_symbols)):
                if c == line_1_symbols[i] and c != "q" and c != "a" and c != "z":
                    print(line_1_symbols[i - 1], end="")
                    pass
                elif c == line_1_symbols[i] and c == "q":
                    print(line_1_symbols[i+9], end="")
                    pass
                elif c == line_1_symbols[i] and c == "a":
                    print(line_1_symbols[i + 8], end="")

                elif c == line_1_symbols[i] and c == "z":
                    print(line_1_symbols[i + 6], end="")

    print()

