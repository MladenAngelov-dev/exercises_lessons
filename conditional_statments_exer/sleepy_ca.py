holy_days = int(input())

year = 365
tom_limit = 30_000

play_time_work = (year - holy_days) * 63
play_time_holy = holy_days * 127

total_time = play_time_work + play_time_holy

if total_time <= tom_limit:
    hours = (tom_limit - total_time) // 60
    minutes = (tom_limit - total_time) % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    hours = (total_time - tom_limit) // 60
    minutes = (total_time - tom_limit) % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
