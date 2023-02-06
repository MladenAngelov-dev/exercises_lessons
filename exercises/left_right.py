line_count = int(input())
num1 = 0
num2 = 0

for _ in range(1, line_count + 1):
    cur_numb = int(input())
    num1 += cur_numb

for nu in range(1, line_count + 1):
    cur_numb2 = int(input())
    num2 += cur_numb2

if num1 == num2:
    print(f"Yes, sum = {num1}")
else:
    print(f"No, diff = {abs(num1 - num2)}")
