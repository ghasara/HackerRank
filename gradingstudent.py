def gradingStudents(grades):
    a=len(grades)
    b=[]
    r=0
    f=0
    v=0
    for i in range(a):
        if grades[i]<38:
            b.append(grades[i])
        else:
            if grades[i]%5==0:
                b.append(grades[i])
            else:
                r=grades[i]%5
                f=5-r
                if f<3:
                    v=grades[i]+f
                    b.append(v)
                else:
                    b.append(grades[i])     
    for i in b:
        print(i)                  

  

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    gradingStudents(grades)
