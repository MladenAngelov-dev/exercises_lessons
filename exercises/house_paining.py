heigh = float(input())
side_wall = float(input())
roof_side = float(input())

side = (heigh * side_wall) * 2 - ((1.5 * 1.5) *2)
front = (heigh * heigh) * 2 - (1.2 * 2)

front_side = front + side
green_paint = front_side / 3.4

roof_square = (heigh * side_wall) * 2
roof_triangle = ((heigh * roof_side) / 2) * 2

toral_roof = roof_square + roof_triangle
red_paint = toral_roof / 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")