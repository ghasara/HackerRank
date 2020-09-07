def arrange():
    for i in range(len(list2)):
        if list2[i].endswith('@gmail.com'):
            a.append(list1[i])
    a.sort(key=lambda x: x.split()[0])
    for i in a:
        print(i)

if __name__=="__main__":
    n=int(input())
    list1=[]
    list2=[]
    a=[]
    for i in range(n):
        n,e=input().split()
        list1.append(n)
        list2.append(e)
    arrange()    
    
