###q8 numbers divisible by 7 and multiply by 5
start=int(input("enter the startof the range"))
end=int(input("enetr the end of range"))
for i in range (start,end+1):
    if i%7 ==0 and i*5 ==0:
        print(i,end=' ')

