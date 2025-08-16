class student:
    id="" 
    name=""
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def display(self):
        print(f"ID is : {self.id}, Name is : {self.name}")


        

Rahim = student(101,"Rahim")
Rahim.display()

karim = student(102,"karim")
karim.display()