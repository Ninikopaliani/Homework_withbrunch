import json

recipies = {"dish_1": ["tomato","coriander", "chia"],"dish_2":["carrot","chilli","spinach"]}
stories = {"shop_1": ["tomato", "carrot"],"shops_2":["chia","coriander"],"shop_3":["chilli", "capsicum"]}

with open("rec_json.json", "w") as file_1:
    json.dump(recipies, file_1)


with open("story_json.json", "w") as file_2:
    json.dump(stories, file_2)


def read_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{filename}'.")
        return None


def find_stores_for_dish(recipes, products):
    dish = input("Enter the dish you want to prepare: ").strip().lower()

    if dish not in recipes:
        print("Error: This dish is not available in the recipes.")
        return

    ingredients = recipes[dish]
    stores = []

    for ingredient in ingredients:
        found = False
        for store, products_available in products.items():
            if ingredient in products_available:
                stores.append(store)
                found = True
                break
        if not found:
            print(f"Error: Ingredient '{ingredient}' not available in any store.")
            return

    return list(set(stores))


def main():
    recipes_file = "rec_json.json"
    products_file = "story_json.json"

    # Read recipes and products data
    recipes = read_json(recipes_file)
    products = read_json(products_file)

    if recipes is None or products is None:
        return

    stores = find_stores_for_dish(recipes, products)

    if stores:
        print("You can collect the ingredients for your dish from the following stores:")
        for store in stores:
            print(store)
    else:
        print("You cannot prepare this dish in this city.")


if __name__ == "__main__":
    main()



