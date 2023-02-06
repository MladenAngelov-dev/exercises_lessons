type_fuel = input()
liters = float(input())

if type_fuel in ["Diesel", "Gasoline", "Gas"]:
    if liters >= 25:
        print(f"You have enough {type_fuel.lower()}.")
    else:
        print(f"Fill your tank with {type_fuel.lower()}!")
else:
    print("Invalid fuel!")
