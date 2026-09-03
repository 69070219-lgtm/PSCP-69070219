"""เกมสะสมแต้ม"""
how_many = int(input())
total = 0
for _ in range(how_many):
    sym = input()
    if sym == "+":
        total += 10
    else:
        total -= 5
print(total)
