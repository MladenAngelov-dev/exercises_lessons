pool_size = int(input())
pipe1 = int(input())
pipe2 = int(input())
time = float(input())

pipe1_liters = pipe1 * time
pipe2_liters = pipe2 * time

total_pool = pipe2_liters + pipe1_liters
percents_pool = total_pool / pool_size * 100

pipe1_perc = pipe1_liters / total_pool * 100
pipe2_perc = pipe2_liters / total_pool * 100
if total_pool <= pool_size:
    print(f"The pool is {percents_pool:.2f}% full."
          f" Pipe 1: {pipe1_perc:.2f}%. Pipe 2: {pipe2_perc:.2f}%.")
else:
    print(f"For {time} hours the pool overflows with {total_pool - pool_size} liters.")
