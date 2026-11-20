n = 5

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    
    for j in range(4, i, -1):
            print(" ",end=" ")
    for j in range(4, i, -1):
            print(" ",end=" ")
            
    for k in range(i+1):
        print("* ", end=" ")
    print()
for i in range(n):
    for j in range(4,i,-1):
        print("*",end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i+1):
            print(" ",end=" ")
    for k in range(4, i,-1):
            print("* ",end=" ")
    print()
            
        