type = input()
liters = float(input())
cart = input()

gasoline = 2.22
diesel = 2.33
gas = 0.93

total = 0

if cart == "Yes":
    if type == "Gasoline":
        gasoline -= 0.18
        total = gasoline * liters
    elif type == "Diesel":
        diesel -= 0.12
        total = diesel * liters
    elif type == "Gas":
        gas -= 0.08
        total = gas * liters
else:
    if type == "Gasoline":
        total = gasoline * liters
    elif type == "Diesel":
        total = diesel * liters
    elif type == "Gas":
        total = gas * liters
if 20 <= liters <= 25:
    total = total * 0.92
elif 25 < liters:
    total = total * 0.90

print(f"{total:.2f} lv.")
