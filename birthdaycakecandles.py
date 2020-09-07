def birthdayCakeCandles(ar):
    n=len(ar)
    ar.sort()
    a=0
    for i in range(n):
        if ar[-1]==ar[i]:
            a+=1
    return a        

if __name__ == '__main__':
    

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    print(result)
