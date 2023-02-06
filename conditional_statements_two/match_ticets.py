budget = float(input())
category = input()
num_fens = int(input())

vip = 499.99
normal = 249.99

price_ticket = 0
transport = 0

if num_fens < 5:
    transport = budget * 0.75
elif num_fens < 10:
    transport = budget * 0.60
elif num_fens < 25:
    transport = budget * 0.50
elif num_fens < 50:
    transport = budget * 0.40
elif num_fens >= 50:
    transport = budget * 0.25

money_left = budget - transport

if category == "VIP":
    price_ticket = vip * num_fens
else:
    price_ticket = normal * num_fens

if money_left >= price_ticket:
    print(f"Yes! You have {money_left - price_ticket:.2f} leva left.")
else:
    print(f"Not enough money! You need {price_ticket - money_left:.2f} leva.")
