grupes = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for i in range(grupes):
    people = int(input())
    if people < 6:
        musala += people
    elif people < 13:
        monblan += people
    elif people < 26:
        kilimanjaro += people
    elif people < 41:
        k2 += people
    else:
        everest += people
total_people = everest + k2 + kilimanjaro + monblan + musala

print(f"{musala/total_people * 100:.2f}%")
print(f"{monblan/total_people * 100:.2f}%")
print(f"{kilimanjaro/total_people * 100:.2f}%")
print(f"{k2/total_people * 100:.2f}%")
print(f"{everest/total_people * 100:.2f}%")
