# Python magic methods
# magicMethods objects niye kaj kor
class Bike:
    def __init__(self,name,color):
        self.name=name 
        self.color=color 
    def __eq__(self,other):
        return self.name==other.name and self.color==other.color
    def __str__(self):
        return (f"{self.name} is {self.color} colored")
    def displayDetails(self):
         print(f"{self.name} is {self.color} colored")
    
bike1=Bike('Yamaha R15',"Red")
bike2=Bike("Yamaha R15","Red")
print(bike1) #Yamaha R15 is Red colored

# print(bike1==bike2) // false
# bike1 and bike2 er value same howya sotteo false return kore. karon == duiti object er value ke compare na kore sorasori duiti object kei compare korche. object reffernce type howyar tader reffernce value alada tai object diutar value same holea false return korche
print(bike1==bike2)
# ekhane true print korbe, karon bike1 and bike2 object ze class theke create hoice sei class e __eq__ function e duita value ke compare kore return kora hoyeche.