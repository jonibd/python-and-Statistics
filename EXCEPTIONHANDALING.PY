# try:
#     list=[20,0,30,4,78,56]
#     result=list[0]/list[3]
#     print(result)
#     print("Done")
# except ZeroDivisionError:
#     print("Dividing by zero is not possible.")
# except IndentationError:
#     print("Your indes is not valid.")
# finally:
#     print("finalir under a joto gula code likhbo sob gula code kaj korbe")

# print("Successful")

# try:
#     num1=int(input("Enter your number:"))
#     num2=int(input("Enter your number:"))
#     result=num2/num2
#     print(result)

# except(ValueError,ZeroDivisionError):
#     print("you have entered incorrect input.")

# finally:
#     print("Thanks !!!")

# def voter (age):
#     if age <18:
#         raise ValueError("Invalid Voter")
#     return "you are allowed to vote"


# try:
#     print(voter(19))
#     print(voter(17))
# except ValueError as e:
#     print(e)