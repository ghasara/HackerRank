s=input()
n=int(input())
length=len(s)
d=n-length
for i in range(d):
    s+=s[i]
print(s.count('a')) 
