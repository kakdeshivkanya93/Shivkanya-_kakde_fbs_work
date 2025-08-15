##q11 strong number
num = int (input("enter a number"))
temp=num
sum=0
while temp>0:
    digit = temp%10
    fact=1
    for i in range(1,digit+1):
        fact*=i

