from math import ceil
from math import floor

mag_num = int(input())
zum_num = int(input())
rose_num = int(input())
cacti_num = int(input())
gift_price = float(input())

mag_price = mag_num * 3.25
zum_price = zum_num * 4
roses_price = rose_num * 3.50
cacti_price = cacti_num * 8

total = (mag_price + zum_price + roses_price + cacti_price) * 0.95
money_left = abs(total - gift_price)

if total >= gift_price:
    money_left = floor(money_left)
    print(f"She is left with {money_left} leva.")
else:
    money_left = ceil(money_left)
    print(f"She will have to borrow {money_left} leva.")
