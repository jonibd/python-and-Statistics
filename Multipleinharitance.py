# class baba:
#     car="BMW"
#     tk="10000000"
#     house="duplex"

# class kaka1:
#     webcamp="iphone"
#     laptop="walton"
#     camera="sony"

# class kaka2:
#     smartphone="iphone"
#     AC="marcel"
#     tab="ipad"


# class kaka(baba,kaka1,kaka2):
#     brokencar="tata" 
#     brokenhouse=" "

# print(kaka.car)
# print(kaka.smartphone)
# print(kaka.laptop)

# class Person:


#     def __init__(self,name,cont,smart_phn):
#         self.name=name
#         self.cont=cont
#         self.smart_phn=smart_phn

    
#     def display(self):

#         print(f"My name is {self.name}.and my contuct number is {self.cont}.I have a {self.smart_phn}")


# class student(Person):
#     id=" "


# st=student("zara","017892939","iphone",'399')
# st.display()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)



class Student(Person):
  def __init__(self, fname, lname,cgpa,id):
    self.cgpa=cgpa
    self.id=id
    super().__init__(fname, lname)

  def printname(self):
    print(self.firstname, self.lastname,self.cgpa,self.id)


x = Person("John", "Doe")
x.printname()  
x = Student("Mike", "Olsen","3.90","399")
x.printname()