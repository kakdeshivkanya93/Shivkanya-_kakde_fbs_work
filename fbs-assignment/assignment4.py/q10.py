###q10  wap number is perfect number
num=int(input("enetr a number:"))
sum =0
for i in range(1,num):
    if num % i == 0:
        sum += i
print('perfect number'if sum== sum  else "not perfect number")

