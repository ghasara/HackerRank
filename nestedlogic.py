d,m,y=map(int,input().split())
d1,m1,y1=map(int,input().split())
d2=d-d1
m2=m-m1
y2=y-y1
c=0
if y2==0:
    if m2>1:
        c=500*m2
    elif m2<0:
        c=0    
    else:
        c=15*d2
elif y2<0:   
    c=0     
else:
    c=1000
print(c) 
