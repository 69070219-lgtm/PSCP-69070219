"""สหกรณ์โรงเรียน"""
member = input()
how_many = int(input())
all_price = 0
for _ in range(how_many):
    price = float(input())
    all_price += price

if member == "Y":
    all_price -= all_price * 0.05
else:
    if all_price >= 500:
        all_price -= all_price * 0.03

print(f"{all_price + 1e-9:.2f}")
