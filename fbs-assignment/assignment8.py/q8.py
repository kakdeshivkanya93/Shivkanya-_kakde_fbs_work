def reverse_number(num):
    return int(str(num)[::-1])

num = int(input("Enter number: "))
print("Reversed number:", reverse_number(num))
