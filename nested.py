#_____#
for i in range(5):
    print(i)

#_________#
for row in range(5):
    for col in range(5):
        print("*" , end=" ")
    print()
    
#__________
for row in range(5):
    for col in range(5):
        print(col,end="")
    print()    
    
    
        
    
#triangle
for row in range(5):
    for col in range(row + 1):
        print("*",end=" ")
    print()
    
    #___
for row in range(5):
    for col in range(row + 1):
        print("*",end=" ")
    print()    
    
    #________#
for row in range(5,0,-1):
    for col in range(row):
        print("*",end=" ")
    print()
    
    #______#
for row in range(5):
    for col in range(5-row-1):
        print("*",end=" ")
    print()
    
    #______#
for row in range(5):
    for col in range(5-row-1):
        print(" ",end= " ")
        for coll in range(row+1):
            print("*",end=" ")
    print()
    
    
    #_________#
    n=int(input("enter the size:"))
    for row in range(5):
        for col in range(5):
            if row == 0 or col == 0 or row == 4-1 or col == 4-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
            
            #______
    n=int(input("enter the size: "))
    for row in range(n):
        for col in range(n):
            if row==col or row==n//5 or row+col==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
        
        # ATM
        
        