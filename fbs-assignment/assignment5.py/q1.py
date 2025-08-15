## q1 correct userid and password chance3 time enter id and pass
userid="admin"
password='pass123'
for i in range(3):
    user_id =input('enter userid')
    pass1=input("enter password")
    if user_id==userid and pass1==password:
        print("login successfully")

