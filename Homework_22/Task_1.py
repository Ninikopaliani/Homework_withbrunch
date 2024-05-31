def data_base(input_file, small_file, high_file):
    with open(input_file, 'r') as data_file, \
         open(small_file, 'w') as small_output, \
         open(high_file, 'w') as high_output:

        for line in data_file:
            user_name, product_name, amount, price = line.strip().split(',')

            amount = int(amount)
            price = int(price)

            if price < 10:
                small_output.write(f"{user_name},{product_name},{amount},{price}\n")
            else:
                high_output.write(f"{user_name},{product_name},{amount},{price}\n")


def main():
    input_file = "data.txt"
    small_file = "small.txt"
    high_file = "high.txt"

    data_base(input_file, small_file, high_file)

    print("please Check 'small.txt' and 'high.txt' for the results.")


if __name__ == "__main__":
    main()
