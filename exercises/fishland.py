skumria = float(input())
caca = float(input())
palamude_kg = float(input())
safride_kg = float(input())
midi_kg = int(input())

palamude_price = (skumria * 1.60) * palamude_kg
safride_price = (caca * 1.80) * safride_kg
midi_price = midi_kg * 7.50

total_price = palamude_price + safride_price + midi_price

print(f"{total_price:.2f}")