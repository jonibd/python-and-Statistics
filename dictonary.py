# dic= {
#     'name ':"jony","id":399,"versity":"bubt"
# }
# print(dic)
# print(dic.keys())
# print(dic.values())

# dic1=dic.copy()
# print("dic1= ",dic1)
# d1=dic['name'] = 'islam'
# print(d1)
# d2=dic['dipertment'] = 'cse'
# print(d2)
# print(dic)
# d3=dic.update({'name':'islam'})
# print(d3)


# dic={
#     "Brand":"ford",
#     "model":"Mustang",
#     "year":1964
#      }
# print(dic["Brand"],dic["model"])

# dic={
#     "Brand":"ford",
#     "model":"Mustang",
#     "year":1964,
#     "year":2030
#      }
# print(dic)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.get("model")
# x = thisdict.keys()
# print(x)
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# #before the change

# car["color"] = "white"

# car.update({"year":2020})

# x1 = car.keys()
# x =car.values()
# print(x1) 
# print(x)


# thisdict={
#     "brand":"Ford",
#     "model":"mustang",
#     "year":1964
# }
# thisdict["color"]="red"
# print(thisdict)
# thisdict.update({"color":"blue"})
# print(thisdict)

# thisdict={
#     "brand":"Ford",
#     "model":"mustang",
#     "YEAR" : 1964
# }

# for x,y in thisdict.items():
#     print(x,y)

# mydict=dict(thisdict)
# print(mydict)


myfamily = {
    "child1":
    { 
        "name":"emil",
    "age":2002

    },
    "child2":
{
    "name":"tobias",
    "age":2008
},
"child3":
{
    "name":"linus",
    "year":2011
}
}

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
