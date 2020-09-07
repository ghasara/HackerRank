l=int(input("enter dimension of frame"))
n=int(input("enter no of total phttos"))
lst1=[]
lst2=[]
for i in range(n):
      s,d=map(int,input("enter no").split())
      lst1.append(s)
      lst2.append(d)
for k,j in [lst1,lst2]:
    if k<l or j<l:
        print("upload another")
    elif k>l or j>l:
        print("crop it")
    else:
        print("accepted")    


      
      
      
      
    
               
