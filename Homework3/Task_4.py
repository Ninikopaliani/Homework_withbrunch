import forex_python.bitcoin
import numbers
from forex_python.bitcoin import BtcConverter
from datetime import datetime
# დაწერეთ პროგრამა რომელიც მიიღებს წელს, თვეს და დღეს, როცა მომხმარებელმა იყიდა ბიტკოინი,
# ასევე მიიღებს დოლარში თანხას, რომელიც შემოყვანილ თარიღში გადაიხადა ბიტკოინის შესაძენად
# და ეკრანზე გამოიტანს დოლარში თანხას რომელიც მოიგო ან დაკარგა დღევანდელი ფასის გათვალისწინებით.

year_of_purchase = int(input("input year of purchase: "))
month_of_purchase = int(input("input month of purchase: "))
day_of_purchase = int(input("input day of purchase: "))
price_of_btc = int(input("input amount of bitcoin (USD$): "))

bought_date = datetime(year_of_purchase, month_of_purchase, day_of_purchase)
current_date = datetime.today()

btc = forex_python.bitcoin.BtcConverter()
bought_price = btc.get_previous_price("USD", bought_date)
current_price = btc.get_latest_price("USD")

paid_per_btc = price_of_btc / bought_price
profit = (paid_per_btc-current_price)/paid_per_btc
if profit >= 0:
    print("your profit is: ", profit)
else:
    print("you lost: ", profit)