"""temp"""
num_temp = float(input())
temp_type = input().lower()
temp_want = input().lower()
if temp_type == 'r':
    temp_C = (num_temp * 5/9) - 273.15
elif temp_type == 'f':
    temp_C = (num_temp - 32) * 5/9
elif temp_type == 'k':
    temp_C = num_temp - 273.15
else:
    temp_C = num_temp
#หาค่าที่ต้องการ
if temp_want == 'r':
    print(f'{(temp_C + 273.15) * 9/5:.2f}')
elif temp_want =='f':
    print(f'{temp_C * 9/5 + 32:.2f}')
elif temp_want == 'k':
    print(f'{temp_C + 273.15:.2f}')
else:
    print(f'{temp_C:.2f}')
