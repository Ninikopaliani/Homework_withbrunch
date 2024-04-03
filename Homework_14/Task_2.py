from Task_1 import gcd_iterative


def lcd(a,b):
    k = (a * b) // gcd_iterative(a, b)
    return k


a = int(input("Enter a: "))
b = int(input("Ender b: "))
print(f"LCD of {a} and {b} is: {lcd(a, b)}")
