#take number of orders
order = int(input("Enter number of Orders : "))
# creating a array
orderArray=[]
for i in range(1,11):
    orderArray.append(i)

print(orderArray)
# owner se puchenge ki kitne approve karenge
approvedOrder = int(input("Owner Please Enter approved orders"))
approvedOrderArray =[]

for i in range(approvedOrder):
    apvalue=int(input("enter approved order"))
    approvedOrderArray.append(apvalue)      

    
    
Users = ["user1","user2","user3","user4"]

managerAssignedUser=input("Manager.. !Please enter assigned User : ")

 
print("All the Orders are Delivered.....")

