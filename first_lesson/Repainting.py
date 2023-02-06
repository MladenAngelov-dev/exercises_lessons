nailon = int(input())
paint = int(input())
cleaner = int(input())
houers_work = int(input())

nailon_price = (nailon+2) * 1.50
paint_price = (paint + ( paint * 0.1)) * 14.50
cleaner_price = cleaner * 5.00
bags = 0.40

materials_total = nailon_price + paint_price + cleaner_price + bags
workers_price = (materials_total * 0.30) * houers_work

print(materials_total+workers_price)