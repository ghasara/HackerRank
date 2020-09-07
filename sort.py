n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(0, n-1): 
        if arr[j] > arr[j+1] : 
            arr[j], arr[j+1] = arr[j+1], arr[j] 
            c+=1     
        
print("Array is sorted in",c,"swaps.")
print("First Element:",arr[0])
print("Last Element:",arr[n-1])
