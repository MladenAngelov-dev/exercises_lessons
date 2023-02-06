actor = input()
academy_pints = float(input())
num_judges = int(input())

oscar_points = 1250.5

for i in range(num_judges):
    judge_name = input()
    judge_points = float(input())
    academy_pints += len(judge_name) * judge_points / 2
    if oscar_points < academy_pints:
        break

if oscar_points <= academy_pints:
    print(f"Congratulations, {actor} got a nominee for leading role with {academy_pints:.1f}!")
else:
    print(f"Sorry, {actor} you need {oscar_points - academy_pints:.1f} more!")
