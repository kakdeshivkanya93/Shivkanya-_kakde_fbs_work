##series of sum
def sum_series_n(n):
    return sum(range(1, n + 1))

n = int(input("Enter n: "))
print("Sum =", sum_series_n(n))


##series of factorial
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def sum_factorial_series(n):
    return sum(factorial(i) for i in range(1, n + 1))

n = int(input("Enter n: "))
print("Sum =", sum_factorial_series(n))



##seris of
def sum_power_series(n):
    return sum(i**i for i in range(1, n + 1))

n = int(input("Enter n: "))
print("Sum =", sum_power_series(n))




