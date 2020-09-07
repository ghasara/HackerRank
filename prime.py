import math

def check_prime(num):
    if num == 1:
        return "Not prime"
    sq = int(math.sqrt(num))
    for x in range(2, sq+1):
        if num % x == 0:
            return "Not prime"
    return "Prime"
if __name__=="__main__":
    n=int(input())
    a=[]
    for i in range(n):
        a.append(check_prime(int(input())))
    for i in a:
        print(i)
                   
