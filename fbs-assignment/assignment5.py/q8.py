###q8
#1.1!+2!+3!...n
n= int (input("enter the number"))
sum=0
for i in range(1,n+1):
    fact=1
    for j in range(1,n+1):
        fact*=j
    sum+=fact
print(f"sum of the series:{sum}")

#2.n+n2+2^3....n
n= int (input("enter the number"))
sum=0
for i in range(1,n+1):
    sum+=n**i
print(f'sum of the series:{sum}')

#3 geometric series with common ratio
n= int (input("enter the number"))
sum=0
for i in range(n):
    sum += 2**i
print(sum)

#4 sum=(a*(r**n-1))/(r-1)
n= int (input("enter the number"))
a=1
r=2
sum=(a*(r**n-1))//(r-1)
print(f'sum of the geometric series')

##5 x-x2/3+x3/5-x4/7...n
x=float(input('enter the value of x:'))
n=int(input("enter the number of terms"))
sum=0
denom=1
for i in range(1,n+1):
    term =(x**i)/denom
    if i%2 ==0:
        term=-term
    sum +=term
    denom +=2
print(f'sum of the series:{sum}')

#6 s=a+a2/2+a3/3+....+a10/10
a=float(input("enter the value of a:"))
sum=0
for i in range(1,11):
    sum+=(a**i)/i
print(f'sum of the series:{sum}')