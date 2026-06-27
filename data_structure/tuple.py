# 1. what is tuple in python
# Ans : A tuple is a collection data type in Python that is ordered and immutable.
# It is similar to a list, but unlike lists, tuples cannot be modified after they are created.
# Tuples are defined using parentheses () and can contain elements of different data types. 


list=[8,5,4,7,6,7,8,9,10] # list is a collection data type in Python that is ordered and mutable. It is defined using square brackets [] and can contain elements of different data types.
tuple1=(8,5,4,7,6,7,8,9,10) # tuple is a collection data type in Python that is ordered and immutable. It is defined using parentheses () and can contain elements of different data types. 
print(tuple1.count(8))
print(tuple1.index(4))

for i in range(len(tuple1)):
    print(tuple1[i])
    
print(tuple1)
