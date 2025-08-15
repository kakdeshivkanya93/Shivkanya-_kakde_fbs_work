##q8
import random
userid = input(" enter user id:")
password=input(" enter password")
user_id = " admin123"
user_password=' 937085'
if(userid==user_id and password==user_password):
    captcha=random.randint(1111,9999)
    print("captcha:",captcha)
    user_captcha = input("enter captcha")
    if(user_captcha==captcha):
        print("login successfully")
    else:
        ("invalid captcha")   
else:
    print("invalid user id or password")             

