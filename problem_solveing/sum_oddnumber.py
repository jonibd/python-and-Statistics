

def sum_of_odd_num(n):
    sum=0
    for i in range(1,n+1):
        if i%2!=0:
            sum+=i
    return sum

n=int(input("Enter the value of n:"))
x=sum_of_odd_num(n)
print(x)