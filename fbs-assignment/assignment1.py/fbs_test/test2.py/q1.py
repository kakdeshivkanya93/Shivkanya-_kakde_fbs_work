##q1 leap year or not
year = int (input("enetr  a year"))
if(year % 4 ==0):
    if(year % 100 ==0):
        if(year% 400 ==0):
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not leap year")


