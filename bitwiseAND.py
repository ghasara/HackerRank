t=int(input())
a1=[]
for _ in range(t):
    a=[]
    s,n=map(int,input().split())
    for i in range(s):
        for j in range(i,s-1):
            c=i&j
            if c<n:
                a.append(c)
                b=max(a)
    a1.append(b) 
for i in a1:
    print(i) 
