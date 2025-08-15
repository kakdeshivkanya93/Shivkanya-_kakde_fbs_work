##q2percentage
# Student 1
s1_m1 = float(input("Enter Student 1 Subject 1 marks: "))
s1_m2 = float(input("Enter Student 1 Subject 2 marks: "))
s1_m3 = float(input("Enter Student 1 Subject 3 marks: "))
s1_m4 = float(input("Enter Student 1 Subject 4 marks: "))
s1_m5 = float(input("Enter Student 1 Subject 5 marks: "))
s1_perc = (s1_m1 + s1_m2 + s1_m3 + s1_m4 + s1_m5) / 5

# Student 2
s2_m1 = float(input("Enter Student 2 Subject 1 marks: "))
s2_m2 = float(input("Enter Student 2 Subject 2 marks: "))
s2_m3 = float(input("Enter Student 2 Subject 3 marks: "))
s2_m4 = float(input("Enter Student 2 Subject 4 marks: "))
s2_m5 = float(input("Enter Student 2 Subject 5 marks: "))
s2_perc = (s2_m1 + s2_m2 + s2_m3 + s2_m4 + s2_m5) / 5

# Output
print(f"Student 1 Percentage: {s1_perc:.2f}%")
print(f"Student 2 Percentage: {s2_perc:.2f}%")
print(f"Average Percentage: {(s1_perc + s2_perc) / 2:.2f}%")












