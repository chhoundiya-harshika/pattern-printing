n = 5

for i in range(n):
    for j in range(i):
        if i == 0 or i == n - 1 or j == 0 or j == i - 1: #inner spacing of logic in triangle
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
