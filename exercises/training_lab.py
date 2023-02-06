wenght = float(input())
height = float(input())

wenght_cm = wenght * 100
height_cm = height * 100 - 100

roles = wenght_cm // 120
coloms = height_cm // 70
num_spaces = roles * coloms - 3

print(int(num_spaces))
