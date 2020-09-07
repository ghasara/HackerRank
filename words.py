n=int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())
for i in range(len(list1)-2):
    c=1
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j]:
            c+=1
    list2.append(c)
list2.append(c)
print(len(list2))
for i in list2:
    print(i,end=" ")
