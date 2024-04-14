temp = [22, 25, 19, 23, 25, 26, 23]
temp_sum = 0
for c in temp:
    temp_sum += c
    avg = temp_sum//len(temp)
print("The average of the temperature is: ",avg)
