arry=[]
n=int(input("Enter your number:"))
for i in range(n):
    num=int(input("Enter your value: "))
    arry.append(num)
print(arry)
devide=[]
for num in arry:
    if num%3==0 and num%5==0:
        devide.append(num)

print(devide)