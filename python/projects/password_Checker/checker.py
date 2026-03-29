def checker(password):
    contain_no = False
    contain_char = False
    if len(password)>=8:
        for i in password:
            if i.isalpha():
                contain_char = True
            if i.isdecimal():
                contain_no = True
        if not (contain_no) or not (contain_char):
            return False
        else:
            return True
    else:
        return False
            
def main():
    password = str(input("enter your password: "))
    while not checker(password):
        print("""Conditions:
• length ≥ 8
• must contain number
• must contain letter""")
        password = str(input("try again: "))
    
    print(f"good password :{password}")

main()
