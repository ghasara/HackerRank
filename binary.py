def decimalToBinary(n):  
    return bin(n).replace("0b", "")  
      

num=int(input())
s=decimalToBinary(num)
burstList=list(s)
counter = 0
output = []
burst_open = False
for i in burstList:
    if int(i) == 1:
        counter += 1
        burst_open = True
    else:
        if burst_open:
            output.append(counter)
        counter = 0
        burst_open = False

if counter !=0:
    output.append(counter)   
output.sort()
out=len(output)
if out>1:
    print(output[out-1])
else:
    print(output[0])
