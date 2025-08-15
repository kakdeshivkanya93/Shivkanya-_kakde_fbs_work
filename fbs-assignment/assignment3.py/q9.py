##q9
age= int(input("enter age:"))
gender= input("enetr gender(m/f):")
if((gender=='m' and age>=21) or (gender=='f' and age>=18)):
    print('eligible to marry')
else:
    print(" not eligible to marry")


