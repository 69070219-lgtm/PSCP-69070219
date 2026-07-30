"""BrickBridge"""
Val_A = int(input())
Val_B = int(input())
goal = int(input())
use_B = min(goal // 5 , Val_B)
another_long = goal - (use_B * 5 )
if another_long <= Val_A:
    print(another_long)
else:
    print(-1)
