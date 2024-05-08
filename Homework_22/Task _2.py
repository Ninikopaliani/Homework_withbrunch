def process_data(input_file):
    users = {}
    total_purchase_cost = 0
    total_purchase_quantity = 0
    products = {}

    with open(input_file, 'r') as data_file:
        for line in data_file:
            user_name, product_name, amount, price = line.strip().split(',')
            amount = int(amount)
            price = float(price)
            total_purchase_cost += price
            total_purchase_quantity += amount

            if user_name in users:
                users[user_name] += amount
            else:
                users[user_name] = amount

            # Part e: Product with the largest number of sales
            if product_name in products:
                products[product_name] += amount
            else:
                products[product_name] = amount

    max_purchase_users = [user for user, purchase in users.items() if purchase == max(users.values())]

    customers = {}
    with open(input_file, 'r') as data_file:
        for line in data_file:
            user_name, _, amount, price = line.strip().split(',')
            amount = int(amount)
            price = float(price)
            total_value = price
            if user_name in customers:
                customers[user_name] += total_value
            else:
                customers[user_name] = total_value
    max_purchase_customers = [customer for customer, value in customers.items() if value == max(customers.values())]

    mean_purchase_cost = total_purchase_cost / total_purchase_quantity

    mean_purchase_quantity = total_purchase_quantity / len(users)

    max_sales_products = [product for product, sales in products.items() if sales == max(products.values())]

    return max_purchase_users, max_purchase_customers, mean_purchase_cost, mean_purchase_quantity, max_sales_products


def main():
    input_file = "data.txt"
    max_purchase_users, max_purchase_customers, mean_purchase_cost, mean_purchase_quantity, max_sales_products = process_data(input_file)

    print("Users with maximum purchases:", max_purchase_users)
    print("Customers with maximum total purchase value:", max_purchase_customers)
    print("Arithmetic mean of the cost of purchases:", mean_purchase_cost)
    print("Arithmetic mean of the purchase quantities:", mean_purchase_quantity)
    print("Products with maximum sales:", max_sales_products)


if __name__ == "__main__":
    main()






