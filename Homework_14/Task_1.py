def gcd_iterative(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    if not (0 < a < 10000) or not (0 < b < 10000):
        print("Invalid input. try again.")
        return

    gcd_iter = gcd_iterative(a, b)
    gcd_recur = gcd_recursive(a, b)

    print(f"GCD of {a} and {b} is: {gcd_iter}")
    print(f"GCD of {a} and {b} is: {gcd_recur}")


if __name__ == "__main__":
    main()





