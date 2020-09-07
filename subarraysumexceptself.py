def miniMaxSum(arr):
    sum=0
    list1=[]
    for i in range(len(arr)):
        sum+=arr[i]
    for i in range(len(arr)):
        list1.append(sum-arr[i])
    list1.sort() 
    print(list1[0],list1[-1])  


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
