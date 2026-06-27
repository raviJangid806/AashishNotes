class car:
    brand=""
    Model=""
    year=""
    
    def inputcardetails(self):
         self.brand=input("enter brand")
         self.model=input("enter model")
         self.year=input("enter year")
     
    def cardetails(self):
        print("carbrand",self.brand)
        print("carmodel",self.model)
        print("caryear",self.year)
        
        
# class to apane ne ban di but use use kase karenge, use use karenge objecct banakar
# sabse pahle object banao
i10 = car()
i10.inputcardetails()
i10.cardetails()


        

                  