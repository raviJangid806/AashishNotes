class human: #class likhte hi class ban jati hai
    # variables (funcationlity)
    legs=2
    hands=2
    # # constructor
    #no paramater
    #self parameter
    # self + tere man mein jo hai wo
    def __init__(self,fdasdg,surname):
        print("class started")
        print(fdasdg,surname)

    # methods (function) (characteristic)
    # private

    #access modiifer:
    # private , kase pata chale ki wo private hai, _
    # public kuch bhi lagane ki jarurat nahi hai
    # protected __
    def dance(self):
        print("public")

    def _dancing():
        print("private")


print("abs")
aashish = human("aashish","prajapat") #creating objects
# ravi = human()
print("line")

# ravi.dance("ravi")
aashish.dance()
print(aashish.legs)

    