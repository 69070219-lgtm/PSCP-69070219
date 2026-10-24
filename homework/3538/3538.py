"""B - Fully pair?"""
s = input()
ans = ""

for i in s:
    if s.count(i) % 2 and i not in ans:
        ans += i
if not ans:
    print("fully paired")
else:
    print(ans)
