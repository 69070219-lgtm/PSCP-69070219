"""สลากกินแบ่ง"""
akson1, num1 = input().split()
akson2, num2 = input().split()
akson1 = akson1.upper()
akson2 = akson2.upper()
total = 0
if (akson1 == akson2) and (num1 == num2):
    total = 1000000
elif (akson1 != akson2) and (num1 == num2):
    total = 100000
else:
    if akson1 == akson2:
        if num1[-3:] == num2[-3:]:
            total = 2000
        elif num1[-2:] == num2[-2:]:
            total = 1000
        elif num1 != num2:
            total = 20
    elif akson1 != akson2:
        if num1[-3:] == num2[-3:]:
            total = 200
        elif num1[-2:] == num2[-2:]:
            total = 100
print(total)
