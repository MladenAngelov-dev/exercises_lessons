from math import ceil

days = int(input())
food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input()) / 1000

dog_needs = dog_food * days
cat_needs = cat_food * days
turtle_needs = turtle_food * days

total_needs = ceil(dog_needs + cat_needs + turtle_needs)
food_left = abs(food - total_needs)

if total_needs <= food:
    print(f"{food_left} kilos of food left.")
else:
    print(f"{food_left} more kilos of food are needed.")
