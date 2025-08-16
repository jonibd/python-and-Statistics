# thisdict={
#     "name":"jony",
#     "age":24,
#     "versity":"BUBT"

# }

# # print(thisdict)
# # print(thisdict["name"])
# # print(thisdict["versity"])
# # thisdict.update({"age":25})
# # print(thisdict)
# # thisdict["roll"]=399
# # print(thisdict)

# for x,y in thisdict.items():
#     print(x,y)


# dic={

# }

# for i in range(3):
#     subject=input("Enter your subject: ")
#     mark=int(input("Enter your marks: "))
#     dic[subject]=mark
# print(dic)
# average=sum(dic.values())/len(dic)
# print(average)
# highet_subject=max(dic,key=dic.get)
# print(highet_subject)


# name_s=[]
# for i in range(5):
#     name=input("Enter your name:")
#     name_s.append(name)

# U_name=set(name_s)

# print(U_name)

# name=input("Enter your name:")
# id=int(input("Enter your id :"))
# depertment=input("Enter your depertment :")

# student=(name,id,depertment)

# print("Student information is:")
# print("name:",student[0])
# print("id:",student[1])
# print("depertment",student[2])



# student={

# }

# for i in range(3):
#     name=input("Enter your name:")
#     marks=int(input("Enter your marks:"))
#     student[name]=marks

# print("Student results list:")
# for name,marks in student.items():
#     print("name:",name)
#     print("marks:",marks)

# scarch_word="jony"
# replace_word="lamim"

# with open(r'text1.text','r') as file:
#     data=file.read()
#     data=data.replace(scarch_word,replace_word)


# with open(r'text1.text','w') as file:
#     file.write(data)