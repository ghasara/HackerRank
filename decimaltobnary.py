def decimalToBinary(n):  
    return bin(n).replace("0b", "")  
      
if __name__ == '__main__':
    num=int(input())
    s=decimalToBinary(num)
    c=0
    for i in range(len(s)):
        if s[i]=='1':
            c+=1
    print(c) 
