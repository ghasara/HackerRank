# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    i=0
    count=0
    ar.sort()
    ar.append('#')
    while i<n:
        if ar[i]==ar[i+1]:
            count+=1
            i+=2
        else:
            i+=1   
    return count         



if __name__ == '__main__':

    n=int(input())
    ar=list(map(int,input().split()))
    print(sockMerchant(n,ar))
