##q12 armstrong number
start=int(input("enter the startof the range"))
end=int(input("enetr the end of range"))
for num in range(start,end+1):
    temp=numsum=0
    digits=len(str(num))
    while temp >0:
        digit = temp