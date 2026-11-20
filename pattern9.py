n = 10

for i in range(n):
   
    for j in range(n - i - 1):
        print(" ", end="") #spacing for above half pyramid
    
    for k in range(i + 1):
        print("* ", end="")
    print()
for i in range(n - 1, -1, -1):
    
    for j in range(n - i - 1):
        print(" ", end="") #spacing for below half pyramid
    
    for k in range(i + 1):
        print("* ", end="")
    print()

   

