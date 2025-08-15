n = 5

# Top half
for i in range(1, n + 1):
    # Leading spaces
    print(" " * (n - i), end="")
    # Stars & hollow space
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Bottom half
for i in range(n - 1, 0, -1):
    # Leading spaces
    print(" " * (n - i), end="")
    # Stars & hollow space
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
