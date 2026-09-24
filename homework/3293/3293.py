"""BigFrame"""
text = []

for i in range(5):
    texts = input()
    text.append(texts)

longest = 0

for i in text:
    if len(i) > longest:
        longest = len(i)

print("*" * (longest + 4))

for i in text:
    print("* " + i + " " * (longest - len(i)) + " *")

print("*" * (longest + 4))
