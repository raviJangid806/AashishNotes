#self ek keyword hai. jo batata hai ki yye kis ke anadar hai
class BankDetail:
    name=""
    acnumber=""
    age=""
    dob=""
    address=""

    def __init__(self):
        print(self.name,self.acnumber,self.age,self.dob,self.address)
    
    def enterDetails(self,name,acnumber,age,dob,address):
        self.name = name
        self.acnumber = acnumber 
        self.address=address
        self.age=age
        self.dob=dob

    def displayDetails(self):
        print()
        print("********Details of Account Holder************")
        print("Name : ",self.name)
        print("Account Number : ",self.acnumber)
        
    def checkValidAccountNumber(self):
        if(len(self.acnumber)==10):
            print("valid")
        else:
            print("Invalid")
    


# create object
aashishAcDetail = BankDetail()
# input acount details
name = input("enter your name :")
number =input("enter ac_number : ")
age =input("enter age : ")
dob =input("enter DOB :")
address =input("enter address : ")
# sari details save object
aashishAcDetail.enterDetails(name,number,age,dob,address)
aashishAcDetail.checkValidAccountNumber()
aashishAcDetail.displayDetails()
print(age)
