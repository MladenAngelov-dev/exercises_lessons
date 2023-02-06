chicken = int(input())
fish = int(input())
vegis = int(input())

chicken_price = chicken * 10.35
fish_price = fish * 12.40
vegis_price = vegis * 8.15

total = chicken_price + fish_price + vegis_price
desert = total * 0.20
full_price = (total + desert + 2.50)

print(full_price)