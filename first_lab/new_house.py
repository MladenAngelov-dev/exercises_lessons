type_flowers = input()
flowers_count =int(input())
budget = int(input())

ROSE_PRICE = 5
DAHLIA_PRICE = 3.8
TULIP_PRICE = 2.8
NARCISSUS_PRICE = 3
GLADIOLA_PRICE = 2.50

total_price = 0

if type_flowers == "Roses":
    total_price = flowers_count * ROSE_PRICE

    if flowers_count > 80:
        total_price *= 0.90

elif type_flowers == "Dahlias":
    total_price = flowers_count * DAHLIA_PRICE

    if flowers_count > 90:
        total_price *= 0.85

elif type_flowers == "Tulips":
    total_price = flowers_count * TULIP_PRICE

    if flowers_count > 80:
        total_price *= 0.85

elif type_flowers == "Narcissus":
    total_price = flowers_count * NARCISSUS_PRICE

    if flowers_count < 120:
        total_price *= 1.15

elif type_flowers == "Gladiolus":
    total_price = flowers_count * GLADIOLA_PRICE

    if flowers_count < 80:
        total_price *= 1.20

if total_price <= budget:
    print(f"Hey, you have a great garden with {flowers_count} {type_flowers}"
          f" and {budget- total_price:.2f} leva left." )
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")