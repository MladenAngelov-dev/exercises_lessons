deposit_sum = int(input())
number_months = int(input())
year_interest = float(input()) / 100

sum_mont = deposit_sum + number_months * ((deposit_sum * year_interest) / 12)

print(sum_mont)