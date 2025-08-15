## q9 wap to print all in range divisible by a given number
start=int(input("enter the startof the range"))
end=int(input("enetr the end of range"))
num=int(input("enter the number"))
for i in range(start,end+1):
    if i%num ==0:
        print(i,end='  ')

