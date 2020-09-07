n,n1=map(int,input().split())
lst=list(map(int,input().split()))
lst1=lst[n1:]+lst[:n1]
for i in lst1:
    print(i,end=" ")
