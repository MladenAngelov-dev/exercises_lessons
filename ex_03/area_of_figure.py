from math import pi

figure = input()
area = 0

if figure == "square":
    side = float(input())
    area = side * side
    print(f"{area:.3f}")

if figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f"{area:.3f}")

if figure == "circle":
    side = float(input())
    area = pi * side ** 2
    print(f"{area:.3f}")

if figure == "triangle":
    side_a = float(input())
    side_b = float(input())
    area = (side_a * side_b) / 2
    print(f"{area:.3f}")
