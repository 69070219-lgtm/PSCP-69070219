"""season"""
month = int(input())
day = int(input())
all_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
if month in all_month:
    if month in [1, 2, 3]:
        if month in [1, 2]:
            print("winter")
        elif month in [3] and day >= 21:
            print("spring")
        elif month in [3] and day < 21:
            print("winter")
    if month in [4, 5, 6]:
        if month in [4, 5]:
            print("spring")
        elif month in [6] and day >= 21:
            print("summer")
        elif month in [6] and day < 21:
            print("spring")
    if month in [7, 8, 9]:
        if month in [7, 8]:
            print("summer")
        elif month in [9] and day >= 21:
            print("fall")
        elif month in [9] and day < 21:
            print("summer")
    if month in [10, 11, 12]:
        if month in [10, 11]:
            print("fall")
        elif month in [12] and day >= 21:
            print("winter")
        elif month in [12] and day < 21:
            print("fall")
