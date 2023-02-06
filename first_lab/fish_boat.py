budget = int(input())
season = input()
fishermen_count = int(input())

total_price = 0

if season == "Spring":
    total_price = 3000
elif season == "Winter":
    total_price = 2600
else:
    total_price = 4200

if fishermen_count <= 6:
    total_price *= 0.90
elif 7 <= fishermen_count <= 11:
    total_price *= 0.85
else:
    total_price *= 0.75

if fishermen_count % 2 == 0 and season != "Autumn":
    total_price *= 0.95

if total_price <= budget:
    print(f"Yes! You have {budget-total_price:.2f}"
          f" leva left.")
else:
    print(f"Not enough money! You need {total_price-budget:.2f} leva.")
