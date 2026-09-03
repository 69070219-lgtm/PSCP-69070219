"""หาจำนวนเฉพาะ"""
start ,stop = map(int,input().split())
Total_primes = 0
all_primes = []
for i in range(start,stop+1):
    if i > 1:
        for l in range(2,i):
            if not i % l:
                break
        else:
            Total_primes += 1
            all_primes.append(i)
if Total_primes > 0:
    print(*all_primes)

print(f"Total primes: {Total_primes}")
