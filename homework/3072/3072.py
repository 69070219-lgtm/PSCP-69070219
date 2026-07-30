"""A-E-I-O-U"""
text = input().lower()
s_ra = ['a' , 'e' , 'i' , 'o' , 'u']
for i in s_ra:
    count = text.count(i)
    if count > 0:
        print(f"{i} : {count}")
