def introTutorial(V,n,arr):
    for i in range(n):
        if arr[i]==V:
            print(i)

if __name__ == '__main__':

    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    introTutorial(V,n,arr)
