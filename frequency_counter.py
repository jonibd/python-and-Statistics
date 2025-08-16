New_list=[]
frequency={}
for i in range(5):
    value=input("Enter your input:")
    New_list.append(value)
for item in New_list:
    if item in frequency:
        frequency[item]+=1
    else:
        frequency[item]=1

print(frequency)
