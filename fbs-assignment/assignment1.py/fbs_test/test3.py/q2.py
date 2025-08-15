##2
n=int(input("enetr the number of terms:"))
sum=0
fact=1
for i in range(1,n+1):
    fact *= i
    sum +=i/fact
print(f"the sum of the series is:{sum}")



