product = input()
day_of_week = input()
num_product = float(input())

price = 0

if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if product == "banana":
        price = num_product * 2.50
    elif product == "apple":
        price = num_product * 1.20
    elif product == "orange":
        price = num_product * 0.85
    elif product == "grapefruit":
        price = num_product * 1.45
    elif product == "kiwi":
        price = num_product * 2.70
    elif product == "pineapple":
        price = num_product * 5.50
    elif product == "grapes":
        price = num_product * 3.85

elif day_of_week in ["Saturday", "Sunday"]:
    if product == "banana":
        price = num_product * 2.70
    elif product == "apple":
        price = num_product * 1.25
    elif product == "orange":
        price = num_product * 0.90
    elif product == "grapefruit":
        price = num_product * 1.60
    elif product == "kiwi":
        price = num_product * 3.00
    elif product == "pineapple":
        price = num_product * 5.60
    elif product == "grapes":
        price = num_product * 4.20

if price != 0:
    print(f"{price:.2f}")
else:
    print("error")
