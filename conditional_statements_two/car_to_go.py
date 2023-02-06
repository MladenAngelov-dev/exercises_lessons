budget = float(input())
sesson = input()

car_budget = 0
car = ""
car_class =""

if budget <= 100:
    car_class = "Economy class"
    if sesson == "Summer":
        car_budget = budget * 0.35
        car = "Cabrio"
    elif sesson == "Winter":
        car_budget = budget * 0.65
        car = "Jeep"
elif budget <= 500:
    car_class = "Compact class"
    if sesson == "Summer":
        car_budget = budget * 0.45
        car = "Cabrio"
    elif sesson == "Winter":
        car_budget = budget * 0.80
        car= "Jeep"
elif budget > 500:
    car_class = "Luxury class"
    car_budget = budget * 0.90
    car = "Jeep"

print(car_class)
print(f"{car} - {car_budget:.2f}")
