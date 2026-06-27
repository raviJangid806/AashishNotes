class student:
    name =""
    rollnumeer =""
    marks =""
    def inputstudentdetails(self):
        self.name=input("enter name")
        self.rollnumber=input("enterollnumbe")
        self.marks=input("entrmars")
        
    def studentdetail(self):
        print("studentname",self.name)
        print("studentrollnumber",self.rollnumber)
        print("studentmarks",self.marks)
        
aashish=student()        
aashish.inputstudentdetails()
aashish.studentdetail()