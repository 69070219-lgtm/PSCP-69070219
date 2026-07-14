"""Bill"""
money = int(input())
service = 0
if 0.1 * money <= 50:
    service = 50
elif 0.1 * money >= 1000:
    service = 1000
else:
    service += 0.1* money
All_bill = money + service
print(f'{((All_bill * 0.07) + All_bill):.2f}')
