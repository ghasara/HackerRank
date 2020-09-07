def minion_game(s):
    v='AEIOU'
    stuart=0
    kevin=0 
    ln = len(s)

    for i in range(ln):  
        if s[i] in v:
            kevin += ln - i
        else:
            stuart += ln - i
        
    if stuart > kevin:
        print('Stuart ', stuart)
        print('Kevin ', kevin)

    elif stuart == kevin:
        print('Draw')
    else:
        print('Kevin ', kevin)
        print('Stuart ', stuart)
minion_game(input())        