def divisor(n):
    div = 0
    for i in range(1, n+1):
        if n % i == 0:
            n//i
            div += 1
        else:
            continue
    return div


def main():
    if divisor(num) == 2:
        print("Simple number!")
    else:
        print("This number isn't simple!")


print("example_1: ")
num = 79
print(num)
main()
print("-"*80)
print("example_2: ")
num = 20
print(num)
main()
print("-"*80)
print("example_3: ")
num = 5
print(num)
main()
