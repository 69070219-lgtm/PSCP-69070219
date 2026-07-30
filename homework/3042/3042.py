"""harn sip"""
The_only_one = int(input())
The_only_one -= The_only_one % 10
output = f'{The_only_one} '
while The_only_one:
    The_only_one = The_only_one - 10
    output += f'{str(The_only_one)} '
print(output)
