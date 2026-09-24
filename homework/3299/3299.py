"""แปลงดอกไม้"""
L, N = map(int, input().split())

diagonal = 0
total = 0

while total < N:
    diagonal += 1
    total += diagonal

print((diagonal + L - 1) // L)
