def solution(s):
    string='abcdefghijklmnopqrstuvwxyz'
    string=list(string)
    s1=list(s)
    list1=[]
    for i in range(len(s1)):
        if s1[i].islower():
            for j in range(len(string)):
                if s1[i]==string[j]:
                    list1.append(string[-(j+1)])
        else:
            list1.append(s1[i])
    list1="".join(list1)
    return list1
if __name__=="__main__":
    print(solution("hii ! u;am"))   
