# def dept():
#     print("data science")
# dept()
# def dept_with_name(name):
#     print(f"my depertment name is {name}")
# dept_with_name("cse")

# def add_num(a,b):
#     result=a+b
#     return result

# sum=add_num(38,80)
# print(sum)

# def user_input():
#     x1=int(input("Enter any value :"))
#     y1=int(input("Enter any value :"))
#     x2=int(input("Enter any value :"))
#     y2=int(input("Enter any value :"))
#     return (x1,y1),(x2,y2)

# r1,r2=user_input()
# print(r1)
# print(r2)

# def multi():
#     x=int(input("x ="))
#     y=int(input("y ="))
#     total=x*y
#     return total

# def multiplication():
#     tutal2 = multi()
#     z=int(input("z ="))
#     total3=tutal2*z
#     print(total3)
# multiplication()

# def fact(x):

#     result = 1
    
#     if x==0 or x==1:
#         print(f"the {x}! is always =1")
#     else:
#         for i in range(x):
#             result*=(i+1)
#         return result
# x=fact(0)
# print(x)


# def fact(x):

#     result = 1
    
#     if x==0 or x==1:
#         print(f"the {x}! is always =1")
#     else:
#        i=1
#        while i <= x:
#           result*=i
#           i=i+1

#        return result
    
# x=fact(5)
# print(x)

#list1=[1,2,3,4,5]
# list2=list1
# list2.insert(0,7)
#print(list1*2)

# x=0
# for i in range(3):
#     x=x+(i%2==0)
# print(x)

# x=[5]
# y=x
# y.append(10)
# x.append(15)
# print(x)

# def function_name(*x):
#     total=0
#     for num in x:
#         total+=num
#     print(total)

# function_name(1,2,3,4)



# def show_details(*args):
#     for i , value in enumerate(args):
#         print(f"{i} th value is:{value}")

# show_details("apple","bananna","cherry")




# def user_info(**kwargs):
#     print(kwargs)

# user_info(name="jony",age=23,city="dhaka")


# def print_ditels(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")
# print_ditels(name="jony",age=23,job="student")

# def print_user(**kwargs):
#     name=kwargs.get("name","Unknown")
#     age=kwargs.get("age",0)
#     print(f"name={name},age:{age}")
# print_user(name="Jony",age=23)

# def mixed_Example(*args,**kwargs):
#     print("args",args)
#     print("kwargs",kwargs)
# mixed_Example(1,2,3,4,name="fahim",age=22)

# def studient_profile(name,*subject,**details):
#     print(F"name:{name}")
#     print("subject:",subject)
#     print("Details",details)
# studient_profile("jony","math","al",age=23,grade="A")

#DEfalt peremitier

# def greet(name="jony"):
#     print(name)
# greet()
# greet("islam")

# def print_items(items):
#     for i in items:
#         print(i)

# print_items(['apple',"mango","bananna","coconut"])

# def calculate(a,b):
#     sum=a+b
#     diff=a-b
#     return sum,diff
# s,d=calculate(10,4)
# print(s)
# print(d)


# squre=lambda x:x*x
# print("squre :",squre(5))

# def outer():
#     print("outer function")
    
#     def inner():
#         print(" inner function")
    
#     inner()

# outer()


# def sum_all(*num):
#     total=0
#     for i in num:
#         total+=i
#     print(total)
# sum_all(1,2,3,4,5,6,7,8,9,10)


# def print_info(**info):
#     for key, value in info.items():
#         print(f"{key} = {value}")

# print_info(name="hanri", age=25, city="dhaka")


# def introduce(name,age):
#     print(F"my name is {name} and i am {age} years old.")
# introduce("jony",23)


# def name_leangth(name):
#     return len(name)
# print("name length is :",name_leangth("jony"))


# def age_cal(brith_year):
#     current_year=2025
#     age=current_year-brith_year
#     return age
    
  
# print(age_cal(2002))


# def format_name(name):
#     return name.capitalize()
# print(format_name("jony"))

# def count_odd(num_list):
#     count=0
#     for i in num_list:
#         if i%2!=0:
#             count+=1
#     return count
# print(count_odd([1,3,4,2,6,45,3,44]))


# def count_letter(word):
#     count=0
#     for i in word:
#         count+=1
#     return count
# print(count_letter('jouijkl'))
# def count_letter(word):
#     count=0
#     for i in range(len(word)):
#         count+=1
#     return count
# print(count_letter('jouijkl'))

# def apply_twice(func,value):
#     return func(func(value))
# def add_five(x):
#     return x+5
# print(apply_twice(add_five,10))



# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     return n * factorial(n-1)
# x=factorial(5)
# print("factorial = ", x)


# def get_info(**student):
#     for key,value in student.items():
#         print(f"{key} : {value}")
# get_info(name="jony",age=23,job="student")


# def sum():
#     print("hello world!")

# sum()


# def sum1(n):
#     sum=0
#     for i in range(n):
#         sum+=i
#     print(sum)
# sum1(10)    


# def student_info(*x):

#     print(x)
   
# student_info("jony",24,"cse")


# def student_info(**args):
    
#     print("my name is " + args["name1"])
#     print("my age is " + args["age1"])

# student_info(name1="jony",age1=24,dep="cse")



# def my_function(name="entizer"):
#     print("I am from " + name)
# my_function("jony")
# my_function("islam")

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)




# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("Recursion Example Results:")
# tri_recursion(7)



# def fact(x):

#     result = 1
    
#     if x==0 or x==1:
#         print(f"the {x}! is always =1")
#     else:
#        i=1
#        while i <= x:
#           result*=i
#           i=i+1

#        return result
    
# x=fact(5)
# print(x)

# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     return n * factorial(n-1)
# x=factorial(5)
# print("factorial = ", x)

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("Recursion Example Results:")
# tri_recursion(6)



