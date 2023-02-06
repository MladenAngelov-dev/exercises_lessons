hrizantemi = int(input())
roses = int(input())
tuleps = int(input())
seasson = input()
hollyday = input()

total_price = 0
num_flowers = hrizantemi + roses + tuleps

if seasson == "Spring" or seasson == "Summer":
    hrizantemi_price = 2.00 * hrizantemi
    roses_price = 4.10 * roses
    tuleps_price = 2.50 * tuleps
    total_price = roses_price + tuleps_price + hrizantemi_price
    if hollyday == "Y":
        total_price *= 1.15
    if tuleps > 7 and seasson == "Spring":
        total_price *= 0.95

else:
    hrizantemi_price = 3.75 * hrizantemi
    roses_price = 4.50 * roses
    tuleps_price = 4.15 * tuleps
    total_price = roses_price + tuleps_price + hrizantemi_price
    if hollyday == "Y":
        total_price *= 1.15
    if seasson == "Winter" and roses >= 10:
        total_price *= 0.90

if num_flowers > 20:
    total_price *= 0.80

print(f"{2 + total_price:.2f}")
