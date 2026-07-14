"""mix colors"""
def mix_colors():
    """Mix colors together"""
    c1 = input("ใส่สีที่ 1 :")
    c2 = input("ใส่สีที่ 2 :")
    All_color = ['Red', 'Yellow', 'Blue']
    if c1 in All_color and c2 in All_color:
        if c1 == 'Red' and c2 == 'Yellow' or c1 == 'Yellow' and c2 == 'Red':
            print("Orange")
        elif c1 == 'Red' and c2 == 'Blue' or c1 == 'Blue' and c2 == 'Red':
            print("Violet")
        elif c1 == 'Yellow' and c2 == 'Blue' or c1 == 'Blue' and c2 == 'Yellow':
            print("Green")
        elif c1 in All_color and c2 in All_color and c1 == c2 and  c2 == c1:
            print(c1)
        elif c1 not in All_color and c2 in All_color and c1 == c2 and c2 == c1:
            print("Error")
    else:
        print("Error")
mix_colors()
