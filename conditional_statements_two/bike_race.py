num_juniors = int(input())
num_seniors = int(input())
race = input()

total_sum = 0
juniors_sum = 0
seniors_sum = 0

if race == "trail":
    juniors_sum = num_juniors * 5.50
    seniors_sum = num_seniors * 7

elif race == "cross-country":
    juniors_sum = num_juniors * 8
    seniors_sum = num_seniors * 9.50
    if num_seniors + num_juniors >= 50:
        juniors_sum = juniors_sum * 0.75
        seniors_sum = seniors_sum * 0.75


elif race == "downhill":
    juniors_sum = num_juniors * 12.25
    seniors_sum = num_seniors * 13.75

elif race == "road":
    juniors_sum = num_juniors * 20
    seniors_sum = num_seniors * 21.50

total_sum = (juniors_sum + seniors_sum) * 0.95
print(f"{total_sum:.2f}")
