n = 5
for i in range(1, n + 1):
    # Leading  spaces
    print("   " * (i - 1), end=" ")
    
    for j in range(i, n + 1):
        if j == i or j == n or i == 1:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

