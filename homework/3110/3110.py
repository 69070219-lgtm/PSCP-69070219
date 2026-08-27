"""สงคราม...ส่งด่วน"""
ton_pray = input()
weight = float(input())
split_ton_pray = ton_pray.split(" ")
TON = str(split_ton_pray[0])
PRAY = str(split_ton_pray[1])

#BKK , CNX , UBP , PKT
if TON == "BKK" and PRAY == "CNX":
    print(f'{weight * 30 + 10:.2f}')
elif TON == "CNX" and PRAY == "UBP":
    print(f'{weight * 40 + 15:.2f}')
elif TON == "UBP" and PRAY == "BKK":
    print(f'{weight * 40 + 20:.2f}')
elif TON == "BKK" and PRAY == "PKT":
    print(f'{weight * 50 + 25:.2f}')
elif TON == "PKT" and PRAY == "CNX":
    print(f'{weight * 60 + 30:.2f}')
elif TON == "UBP" and PRAY == "PKT":
    print(f'{weight * 70 + 40:.2f}')
else:
    print("Error")
