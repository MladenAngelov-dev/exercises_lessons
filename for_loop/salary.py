lines = int(input())
salary = int(input())

FB = 150
IG = 100
RD = 50

for i in range(lines):
    site = input()
    if site == "Facebook":
        salary -= FB
    elif site == "Instagram":
        salary -= IG
    elif site == "Reddit":
        salary -= RD
    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)
