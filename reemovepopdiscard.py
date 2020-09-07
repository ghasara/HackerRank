n = input()
s = set(map(int,input().split()))
n1=int(input())
sum=0
for i in range(n1):
    r=input().split()
    if r[0]=='remove':
        s.remove(int(r[1]))
    elif r[0]=='discard':
        s.discard(int(r[1]))
    else:
        s.pop()
for i in s:
    sum+=int(i)
print(sum)  
