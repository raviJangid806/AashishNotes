# a=2
# b=2
# print(a is b)
# c=[2,4,1,7]
# d=[6,7,3,9]
# print(a in c)


# a number is prime or not

# for a in range(6,101):
#     val=0
#     n1= (a-1)%6
#     n2 = (a+1)%6
#     if(n1==0):
#         if(a%5==0):
#             print(a," is not prime number")
#         else :
#             val=1
#             print(a," is prime number")
#     if(n2==0):
#         if(a%5==0):
#             print(a," is not prime number")
#         else :
#             val=1
#             print(a," is prime number")
#     if(val==0):
#          print(a," - is not prime number")


n1= (a-1)%6
n2 = (a+1)%6
if(n1==0):
    if(a%5==0):
        print(a," is not prime number")
    else : 
        val=1
        print(a," is prime number")
if(n2==0):
    if(a%5==0):
        print(a," is not prime number")
        else :
            val=1
            print(a," is prime number")