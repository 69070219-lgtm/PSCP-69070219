""""ไพ่ 44 ใบ"""
card = input()

first = card[:-1].upper()
second = card[-1].upper()
#print(first, second)
if first == "A":
    first = "ace"
elif first == "J":
    first = "jack"
elif first == "Q":
    first = "queen"
elif first == "K":
    first = "king"

if second == "D":
    second = "diamonds"
elif second == "H":
    second = "hearts"
elif second == "S":
    second = "spades"
elif second == "C":
    second = "clubs"

print(first,"of",second)
