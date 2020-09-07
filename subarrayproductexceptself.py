list1=list(map(int,input().split()))
c=1
j=[]
for i in range(len(list1)):
    c*=list1[i]
for i in list1:
    print(c//i,end=" ")
