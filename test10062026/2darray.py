a=[
  [1,4,3,2],
  [2,2,0,4],
  [3,1,4,1],
  ]
b=0
for i in range(0,3):
    for j in range(0,4):
        print(a[i][j], end=" ")
        if(a[i][j]==0):
            b=b+1
    print(" ")
print(b)    
    