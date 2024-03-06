import datetime

year = int(input("შეიყვანე დაბადების წელი: "))
month = int(input("შეიყვანე დაბადების თვე: "))
day = int(input("შეიყვანე დაბადების დღე: "))

weekday = (datetime.date(year, month, day))

if datetime.date.weekday(weekday) == 6:
    print("Sunday")
elif datetime.date.weekday(weekday) == 0:
    print("Monday")
elif datetime.date.weekday(weekday) == 1:
    print("Tuesday")
elif datetime.date.weekday(weekday) == 2:
    print("Wednesday")
elif datetime.date.weekday(weekday) == 3:
    print("Thursday")
elif datetime.date.weekday(weekday) == 4:
    print("Friday")
else:
    print("Saturday")
    