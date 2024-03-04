user_name = input("შეიყვანე სახელი: ")
user_birth_year = input("შეიყვანე დაბადების წელი: ")
user_birth_year_int = int(user_birth_year)
today_year = 2024
user_age = today_year - user_birth_year_int
print("გამარჯობა,", user_name, ",", "თქვენ ხართ", user_age, "წლის")

