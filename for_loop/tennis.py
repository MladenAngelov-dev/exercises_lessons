num_tour = int(input())
start_points = int(input())

W = 2000
F = 1200
SF = 720

total_points = start_points
wins = 0
for i in range(num_tour):
    placement = input()
    if placement == "W":
        total_points += W
        wins += 1
    elif placement == "F":
        total_points += F
    elif placement == "SF":
        total_points += SF

avarege = (total_points - start_points) / num_tour
win_perc = wins / num_tour * 100

print(f"Final points: {total_points}")
print(f"Average points: {int(avarege)}")
print(f"{win_perc:.2f}%")
