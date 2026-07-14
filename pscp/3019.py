"""safe lock"""
def safe_lock():
    """Safe lock"""
    get_password_1 = input("ตัวอักษร :")
    get_password_2 = input("ตัวเลข :")
    password_1 = 'H'
    password_2 = "4567"
    if password_1 == get_password_1 and password_2 == get_password_2:
        print("safe unlocked")
    elif password_1 == get_password_1 and password_2 != get_password_2:
        print("safe locked - change digit")
    elif password_1 != get_password_1 and password_2 == get_password_2:
        print("safe locked - change char")
    else:
        print("safe locked")
safe_lock()
