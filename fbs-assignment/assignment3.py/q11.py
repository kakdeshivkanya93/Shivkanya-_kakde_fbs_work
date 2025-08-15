##q11
num_people= int(input("enter number of person"))
ticket_amount = float(input("enter tiket amount per person"))
total_amt = num_people*ticket_amount
for i in range(num_people):
    age = int(input(f"enter age of person {i+1}:"))
    if age <= 12:
        total_amt *= 0.3
    elif age>= 59:
        total_amt *= 0.5  
print("total amount:", total_amt)  


