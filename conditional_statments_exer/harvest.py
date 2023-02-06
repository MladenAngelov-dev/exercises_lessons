from math import ceil

land = int(input())
grapes = float(input())
req_wine = int(input())
workers = int(input())

grape_kg = (land * grapes) * 0.40
wine_liters = ceil(grape_kg / 2.5)

if wine_liters >= req_wine:
    workers_wine = ceil((wine_liters - req_wine) / workers)
    print(f"Good harvest this year! Total wine: {wine_liters} liters.")
    print(f"{wine_liters-req_wine} liters left -> {workers_wine} liters per person.")
else:
    print(f"It will be a tough winter! More {ceil(req_wine - wine_liters)} liters wine needed.")
