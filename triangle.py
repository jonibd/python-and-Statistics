# class Triangle:
#     def __init__(self,base,hight):
#         self.base=base
#         self.hight=hight


#     def calculate_area(slfe):
#         area= (.5)*slfe.base*slfe.hight
#         print(area)



# t1=Triangle(4,5)
# t1.calculate_area()
# t2=Triangle(5,8)
# t2.calculate_area()



class Triangle:
    def __init__(self,base,hight):
        self.base=base
        self.hight=hight

    
    def calculate_area(self):

        area=.5*self.base*self.hight

        print("Area is = ",area)

x=Triangle(4,5)
x.calculate_area()