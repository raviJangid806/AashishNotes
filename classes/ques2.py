class rectangle:
    length=0
    width=0
    def inputDimensions(self):
        self.length=int(input("enterlength"))
        self.width=int(input("enterwidth"))
        
    def calculatearea(self):
        print(self.length*self.width)
        
    def calculateperimeter(self):
        print(2*(self.length + self.width))
        
    
room=rectangle()
room.inputDimensions()
room.calculatearea()
room.calculateperimeter()
        
        
        
        
           
        
    

    