#inverted pyramid
n = 5

for i in range(n - 1, -1, -1):
    
    for j in range(n - i - 1):
        print(" ", end="") #spacing
    
    for k in range(i + 1):
        print("* ", end="")
    print()
