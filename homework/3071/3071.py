"""[A,B]"""
start = int(input())
stop = int(input())
d = int(input())
r = int(input())
count = 0
for x in range(start, stop + 1):
    if x % d == r:
        count += 1
print(count)
