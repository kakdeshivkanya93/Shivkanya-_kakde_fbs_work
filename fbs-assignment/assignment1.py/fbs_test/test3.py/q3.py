##q3
n=int(input("enter the number of employees:"))
for i in range(n):
    print(f'\n employee{i+1}')
    basic_salary=float(input("enetr basic salary"))
if basic_salary<20000:
    da=0.10*basic_salary
    ta=0.12*basic_salary
    hra=0.25*basic_salary
else:
    da=0.15*basic_salary
    da=0.18*basic_salary
    da=0.20*basic_salary
total_salary=da+ta+hra
print(total_salary)


