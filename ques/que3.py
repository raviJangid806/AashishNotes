n=int(input("enter a number"))
for x in range(1,n):
    for y in range(1,x+1):
        print("*",end="")
    x=(x+1) 
    print()    
