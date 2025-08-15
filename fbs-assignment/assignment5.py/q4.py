##q4 armstrong number
num=int(input("enter a number"))
sum=0
for digit in str(num):
    sum+=int(digit)**len(str(num))
if num ==sum:
    print(f"{num} is an armstrong number")
else:
    print(f'{sum}')


