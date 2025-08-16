number=[12,78,39,20,78,29,10]
new_list=[]
for i in number:
    if i%2!=0:
        new_list.append(i)
print(new_list)

number=[12,78,39,20,78,29,10]
new_list=[]
for i in number:
    if i%2==0:
        new_list.append(i)
print(new_list)