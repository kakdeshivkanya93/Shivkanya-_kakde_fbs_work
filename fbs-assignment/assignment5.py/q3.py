##q3
num_passengers= int(input("enter number of passengers"))
tikit_cost=float(input("enter tikit cost"))
total_amount =0
for i in range(num_passengers):
    age=int(input(f'enter age of passengers{i+1}:'))
    if age<12:
        discount= 0.30
    elif age>59:
        discount=0.50
    else:
        discount= 0.0
cost_after_discount = tikit_cost*(1-discount)
total_amount+= cost_after_discount
print(total_amount)

