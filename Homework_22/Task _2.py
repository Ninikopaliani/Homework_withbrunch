import json


def data_base(input_file):
    with open(input_file, 'r') as data_file:
        user = []
        total_quantity = 0
        total_price = 0
        product = []

        for line in data_file:
            user_name, product_name, quantity, price = line.strip().split(',')
            quantity = int(quantity)
            price = int(price)
            total_quantity += quantity




