import datetime

__year = int(input("შეიყვანე დაბადების წელი: "))
__month = int(input("შეიყვანე დაბადების თვე: "))
__day = int(input("შეიყვანე დაბადების დღე: "))

__weekday = (datetime.date(__year, __month, __day))

if datetime.date.weekday(__weekday) == 6:
    print("Sunday")
elif datetime.date.weekday(__weekday) == 0:
    print("Monday")
elif datetime.date.weekday(__weekday) == 1:
    print("Tuesday")
elif datetime.date.weekday(__weekday) == 2:
    print("Wednesday")
elif datetime.date.weekday(__weekday) == 3:
    print("Thursday")
elif datetime.date.weekday(__weekday) == 4:
    print("Friday")
else:
    print("Saturday")