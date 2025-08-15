# Program 5: Compound Interest
P = float(input("Enter Principal amount: "))
T = float(input("Enter Time (in years): "))
R = float(input("Enter Rate of interest: "))

CI = P * ((1 + R/100) ** T) - P
print("Compound Interest =", CI)
