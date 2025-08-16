class vaical:
    def __init__(self,name,modle,component):
        self.name=name
        self.modle=modle
        self.component=component

class bus(vaical):
    pass

class car(vaical):
    pass

class bike(vaical):
    pass

b1=bus("volvo","hino","ac_bus")
print(b1.name,b1.modle,b1.component)

b1=car("BMW","1960","eore_wheel")
print(b1.name,b1.modle,b1.component)

b1=bike("r1","2024","two_wheel")
print(b1.name,b1.modle,b1.component)