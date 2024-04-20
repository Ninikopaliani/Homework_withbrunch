my_tuple = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))


def weekly_temp(x):
    daily_min_temp = ()
    daily_max_temp = ()
    daily_avg_temp = ()
    for i in x:
        daily_min_temp += min(i),
        daily_max_temp += max(i),
        daily_avg_temp += sum(i)//len(i),
    weekly_avg_temp = sum(daily_avg_temp)//len(daily_avg_temp)
    return daily_min_temp, daily_max_temp, daily_avg_temp, weekly_avg_temp


def main():
    min_temp, max_tem, avg_tem, weekly_avg = weekly_temp(my_tuple)
    print("daily min temperature for the week: ", min_temp)
    print("daily max temperature for the week: ", max_tem)
    print("daily average temperature for the week: ", avg_tem)
    print("weekly average temperature is: ", weekly_avg)


if __name__ == '__main__':
    main()







