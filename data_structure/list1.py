# list=[1,5,4,7,6,7,8,9,10]
# for i in range(0,len(list)):
#     print(list[i])

# # len(array) : array ki size
# # range(start,end,jump)
# # man le koi list hai or apan uske kisi element ko access karna chahte hai to uske index se access kar sakte hai
# list=[1,5,4,7,6,7,8,9,10]
# list_0th_element=list[0] # list ke 0th index pe jo element hai usko list0thelement variable me store kar diya
# print(list[0]) # 1 apan ne list ke 0th index pe jo element hai usko print kar diya

# string1="hello world" #string1 is a string variable which contains the value "hello world"
# char1='a' # char1 is a character variable which contains the value 'a'
# int1=10 # int1 is an integer variable which contains the value 10
# float1=3.14 # float1 is a floating-point variable which contains the value 3.14

# print("my name is aashish") # print is a function which is used to print the output on the console
# # variable not be in double quotes or single quotes
# print(string1)
# print("string1")


# for i in range(0,len(list)):
#     # first iteration me i ki value 0 hogi to list[0] print hoga jo ki 1 hai
#     print(list[i]);
    
# # chalo dekhte hai ki ye for loop kaise kaam karta hai
# # for loop me range function ka use kiya jata hai jisme start, end aur jump value di jati hai
# # for loop me i variable ko range function ke start se end tak increment kiya jata hai aur har iteration me i ki value print ki jati hai.


# #  list ke functions
list=[8,5,4,7,6,7,8,9,10] #list mein index 0 se 8 tak element hai
# 0th index pe 8,
# 1st index pe 5, 
# 2nd index pe 4,
# 3rd index pe 7,
# 4th index pe 6,
# 5th index pe 7,
# 6th index pe 8,
# 7th index pe 9,
# 8th index pe 10
# .append() : is function ka use list ke end me element add karne ke liye kiya jata hai
# list.append(11) # list ke end me 11 add kar diya
print("COUNT OF 7:",list.count(7)) # list me 7 kitni baar aata hai usko count kar diya
print("INDEX OF 6:",list.index(6)) # list me 6 kitne index pe hai usko print kar diya
print("SIZE OF LIST:",len(list)) # list ki size print kar diya
list.insert(0,1) # list ke 0th index pe 1 add kar diya


print("LIST:",list)
print("SIZE OF LIST:",len(list)) # list ki size print kar diya
print(list.sort()) # list ko sort kar diya
print("SORTED LIST:",list) # sorted list print kar diya
