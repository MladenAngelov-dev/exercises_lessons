pen_pack = int(input())
marker_pak = int(input())
litters_cleaner = int(input())
discount = float(input()) / 100

pen_pack_price = pen_pack * 5.80
marker_pak_price = marker_pak * 7.20
litters_cleaner_price = litters_cleaner * 1.2

full_price = (pen_pack_price + marker_pak_price + litters_cleaner_price)
discount_price = full_price - (full_price * discount)

print(discount_price)
