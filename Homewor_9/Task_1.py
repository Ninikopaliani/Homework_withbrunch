# დაწერეთ პროგრამა რომელიც  მიიღებს სტრიქონი
# და დაადგენს ეს ტექსტი არის თუ არა პალინდრომი.
# Პალინდრომი არის სიტყვა რომელიც მარცხნიდან და მარჯვნიდან ერთნაირად იკითხება.
# Მაგალითად:radar, level, racecar არის პალინდრომები.
# Პროგრამამ უნდა დააიდენტიფიციროს პალინდრომი წინადადებაც.
# Წინადადებიდან უნდა უგულებელყოს ყველა სიმბოლო, გარდა ინგლისური სიმბოლოსებისა a-z, A-Z.
# Პროგრამამ უნდა უგულებელყოს სიმბოლოს რეგისტრი, Racecar არის პალინდრომი.
# მაგალითი 1.
# Input: racecar
# Output: Is palindrome
#
# მაგალითი 2.
# Input: Python
# Output: Is not palindrome
#
# მაგალითი 3.
# Input: Was it a car or a cat I saw?
# Output: Is palindrome
#
# Მაგალითი 4.
# Input: No lemon, no melon!
# Output: Is palindrome





input_text = input("input: ")
input_text_change = input_text.replace(" ", "")  # მოვაშორეთ სიცარიელებები
# if input_text_change.isalpha() is False:  # მოვაშორეთ ყველა სიმბოლო რაც არ იყო ინგლისური ანბანიდან
c = 0
while c < len(input_text_change):
    if input_text_change[c].isalpha() is False:
        k = input_text_change[c]
        input_text_change = input_text_change.replace(k, "")
    c += 1
input_text_change = input_text_change.lower()  # გავასწორე ყველა ერთ რეგისტრში
output_text = input_text_change[::-1]    # შევაბრუნე სიტყვა
if input_text_change == output_text:
    print("output: Is palindrome")
else:
    print("output: Is not palindrome")
