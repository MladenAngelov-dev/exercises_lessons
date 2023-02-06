lines_number = int(input())
odd = 0
even = 0
for num in range(1, lines_number + 1):
    curr_bumber = int(input())
    if num % 2 == 0:
        even += curr_bumber
    else:
        odd += curr_bumber
if odd == even:
    print(f"Yes\n"
          f"Sum = {even}")
else:
    print(f"No\n"
          f"Diff = {abs(odd - even)}")
