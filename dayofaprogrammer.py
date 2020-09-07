def dayOfProgrammer(year):
    c=0
    if (year % 4) == 0:
        if (year % 100) == 0:
           if (year % 400) == 0:
                c=1
           else:
                c=0
        else:
            c=1
    else:
        c=0
    if c==1:
        print("12.09.",year,sep="")
    else:
        print("13.09.",year,sep="")       



if __name__ == '__main__':
   

    year = int(input().strip())

    result = dayOfProgrammer(year)
