years = int(input())
wash_mach = float(input())
toy_price = int(input())

gifted_money = 10
total_money = 0

for age in range(1, years + 1):
    if age % 2 == 0:
        total_money += gifted_money - 1
        gifted_money += 10
    else:
        total_money += toy_price

if total_money >= wash_mach:
    print(f"Yes! {total_money - wash_mach:.2f}")
else:
    print(f"No! {wash_mach - total_money:.2f}")
