def superDigit(n, k):
    n=list(str(n))
    sum=0
    for i in range(len(n)):
        sum+=int(n[i])
    k-=1  
    if k==0:
        return sum
    else:
        return superDigit(sum,k)  


if __name__ == '__main__':
    

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)
