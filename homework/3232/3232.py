"""กบน้อยกระโดด"""
x, y = map(int, input().split())
jump_count = 0
howfarnow = 0

while howfarnow < y and x > 0:
    howfarnow += x
    jump_count += 1
    x -= 2

if howfarnow >= y:
    print(jump_count)
else:
    print(-1)
