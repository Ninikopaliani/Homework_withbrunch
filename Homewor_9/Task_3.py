# 3. დაწერეთ პროგრამა რომელიც მიიღებს თარიღს.
# Პროგრამამ თარიღი უნდა გადაიყვანოს განსხვავებულ ფორმატში და დაბეჭდოს ეკრანზე.
# Შემომავალი და გამომავალი თარიღების ფორმატები იხილეთ მაგალითებში.
# მაგალითი 1.
# Input: 2024-03-22T19:17:42.956376+00:00
# Output: 22-03-2024 7:17:42 +0
#
# მაგალითი 2.
# Input: 2024-03-04T11:17:42.000123+04:00
# Output: 04-03-2024 11:17:42 +4
#
# მაგალითი 3.
# Input: 2024-11-14T15:17:42.123000-03:00
# Output: 14-11-2024 3:17:42 -3



s = input("Input: ")
out_1 = s.replace(s[8:10], s[0:4], 1)
out_2 = out_1.replace(out_1[0:4], s[8:10], 1)
out_3 = out_2.replace("T", " ")
if int(out_3[out_3.find(" ") + 1:out_3.find(" ") + 3]) > 12:
    out_4 = int(out_3[out_3.find(" ") + 1:out_3.find(" ") + 3]) - 12
    out_4 = str(out_4)
else:
    out_4 = out_3[out_3.find(" ") + 1:out_3.find(" ") + 3]
out_5 = out_3.replace(out_3[11:13], out_4, 1)
out_6 = out_5.replace(out_5[out_5.find("."):out_5.find(".") + 7], " ", 1)
if out_6[-6] == "+":
    out_7 = out_6.replace(out_6[out_6.find("+") + 1:out_6.find("+") + 6], out_6[out_6.find("+") + 2])
else:
    out_7 = out_6.replace(out_6[out_6.find("-", 17) + 1:out_6.find("-", 17) + 6], out_6[out_6.find("-", 17) + 2])

print("Output: ", out_7)


