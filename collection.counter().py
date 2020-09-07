n=int(input())
arr=list(map(int,input().split()))
n1=int(input())
list1=[]
list2=[]
money=0
for i in range(n1):
    s,s1=map(int,input().split())
    list1.append(s)
    list2.append(s1)
for i in range(n1):
    for j in range(n):
        if list1[i]==arr[j]:
            money+=list2[i]
            arr.pop(j)
            arr.append(000)
            break 
print(money)  
