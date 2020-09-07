def calculator(i,j,k):
    if j=='+':
        print(i+k)
    elif j=='-':
        print(i-k)
    elif j=='*':
        print(i*k)
    elif j=='/':
        print(i//k)
    else:
        print("no output")


n,v,n1=int(input()),input(),int(input())
calculator(n,v,n1)
