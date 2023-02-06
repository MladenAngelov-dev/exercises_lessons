import sys

num_lines = int(input())

max_num = -sys.maxsize
sum_number = 0

for i in range(num_lines):
    num = int(input())

    if num > max_num:
        max_num = num

    sum_number += num

if max_num == sum_number - max_num:
    print(f"Yes\n"
          f"Sum = {max_num}")
else:
    print(f"No\n"
          f"Diff = {abs(max_num - (sum_number- max_num))}")
