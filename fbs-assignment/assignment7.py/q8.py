k = 7
for i in range(1, 6):
    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end=' ')
    
    # Spaces
    for j in range(1, k + 1):
        print(' ', end=' ')
    k -= 2  # Reduce spaces each row
    
    # Decreasing numbers
    for j in range(i, 0, -1):
        print(j, end=' ')
    
    print()
