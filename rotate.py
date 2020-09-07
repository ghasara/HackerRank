s=input().split(",")
lst=[]
lst1=[]
for i in s:
    s1,n=i.split(":")
    lst.append(s1)
    lst1.append(n)
def rotate(s,n):
    n=list(str(n))
    st=0
    for i in n:
        st+=int(i)**2
    if st%2==0:
        return s[-1:]+s[:-1]
    else:
        return s[2:]+s[:2]
for i in range(len(lst1)):
    print(rotate(lst[i],lst1[i]),end="")
    if i==0:
        print(",",end="")

    
