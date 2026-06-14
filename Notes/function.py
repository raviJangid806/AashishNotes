# what is function : A function is a block of organized, reusable code that is used to perform a single, related action. 
# Functions provide better modularity for your application and a high degree of code reusing. In Python, functions are defined 
# using the `def` keyword, followed by the function name and parentheses containing any parameters.
#  The code block within every function starts with a colon (:) and is indented.


# function start here
def voterAllow():
    age=int(input("enter a number"))
    if(age>=18):
        print("they can vote")
    else:
        print("no")

# function end here


#start here
def cow(name):
    print("this is a cow name",name)

#end here

cow("moti")
voterAllow()