lines = int(input())

p1, p2, p3, p4, p5, = 0, 0, 0, 0, 0,

for i in range(lines):
    number = int(input())
    if number < 200:
        p1 += 1
    elif number < 400:
        p2 += 1
    elif number < 600:
        p3 += 1
    elif number < 800:
        p4 += 1
    else:
        p5 += 1

print(f"{p1 / lines * 100:.2f}%")
print(f"{p2 / lines * 100:.2f}%")
print(f"{p3 / lines * 100:.2f}%")
print(f"{p4 / lines * 100:.2f}%")
print(f"{p5 / lines * 100:.2f}%")