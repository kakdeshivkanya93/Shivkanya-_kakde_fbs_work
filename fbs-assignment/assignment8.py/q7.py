def sum_of_digits(num):
    return sum(int(d) for d in str(num))

num = int(input("Enter number: "))
print("Sum of digits:", sum_of_digits(num))
