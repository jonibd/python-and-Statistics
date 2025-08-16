# class student:
#     id="" 
#     name=""

#     def display(self):
#         print(f"ID is : {self.id}, Name is : {self.name}")

# Rahim = student()
# Rahim.id=101
# Rahim.name="Rahim"
# Rahim.display()

# karim = student()
# karim.id=102
# karim.name="karim"
# karim.display()

class student:
    id="" 
    name=""
    def set_value(self,id,name):
        self.id=id
        self.name=name

    def display(self):
        print(f"ID is : {self.id}, Name is : {self.name}")

Rahim = student()
Rahim.set_value(101,"Rahim")
Rahim.display()

karim = student()
karim.set_value(102,"karim")
karim.display()