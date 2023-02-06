km = int(input())
time = input()

price = 0

if km < 20:
    if time == "day":
        price = km * 0.79 + 0.70
    elif time == "night":
        price = km * 0.90 + 0.70
elif km < 100:
        price = km * 0.09
else:
    price = km * 0.06

print(f"{price:.2f}")
