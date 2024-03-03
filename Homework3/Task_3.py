import random

Card_color = ["hurt","diamonds","spades","clubs"]
Card_symbols = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]

random_color = random.choice(Card_color)
random_symbols = random.choice(Card_symbols)

print(random_color,random_symbols)