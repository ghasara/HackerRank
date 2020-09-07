def plusMinus(arr):
    k=len(arr)
    a=0
    b=0
    c=0
    for i in arr:
        if i<0:
            a+=1
        elif i>0:
            b+=1
        else:
            c+=1 
    print(b/float(k))
    print(a/float(k))  
    print(c/float(k))                 

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
