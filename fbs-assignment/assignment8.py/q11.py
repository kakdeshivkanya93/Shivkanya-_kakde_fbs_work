def is_armstrong(num):
    power = len(str(num))
    return num == sum(int(d)**power for d in str(num))

num = int(input("Enter number: "))
print("Armstrong number?", is_armstrong(num))
