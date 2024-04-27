
cache = {}


def generate_sequence(n):
    sequence = [n]
    if n in cache:
        return cache[n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        sequence.append(n)

    return sequence


def main():
    n = int(input("Enter sequence number: "))
    sequence = generate_sequence(n)

    print("Sequence:")
    print(*sequence)  


if __name__ == "__main__":
    main()

