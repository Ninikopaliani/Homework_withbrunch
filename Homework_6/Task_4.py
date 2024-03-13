n = 5
i = 1
while i < n * 2:
    j = 1
    if i <= n:
        while j <= i:
            print(f"{j}" , end=" ")
            j += 1
    else:
        while j < 2 * n - i:
            print(f"{j}", end=" ")
            j += 1
    print()
    i += 1

