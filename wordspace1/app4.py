class Vehicle:
    def __init__(self,maker,model):
        self.maker=maker
        self.model=model
    def printingMessage(self):
        return f"The model is {self.model} and its maker is {self.maker}"
   
class Car(Vehicle):
    def __init__(self,maker,model,doors):
        super().__init__(maker,model)
        self.doors=doors
    def infoPrinting(self):
        return(f"The maker is: {self.maker}, the model is: {self.model} and has {self.doors} ")
      

class Truck(Vehicle):
    def __init__(self,maker,model,weight):
        super().__init__(maker,model)
        self.weight=weight
    def infoPrinting(self):
        return(f"The maker is: {self.maker}, the model is: {self.model} and weight {self.weight} ")


vehicleObject=Vehicle('Generic','modelTX')
carObject=Car('Toyota','Yaris',3)
truckObject=Truck('Hino','GH',120)

print(vehicleObject.printingMessage())
print(carObject.infoPrinting())
print(truckObject.infoPrinting())




print("***************************************")

class Book:
    def __init__(self,title,author,available):
        self.title=tittle
        self.author=author
        self.available=available



class Library:
    def __init__(self):
        self.books = []