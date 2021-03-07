def grading_student():
    n = int(input().strip())  #number of test cases

    grades = []

    for i in range(n):
        grades_item = int(input().strip())
        grades.append(grades_item)
    
    res = []
    
    for grade in grades:
        if grade>=38:
            m=grade%5
            if m>=3:
                grade+=(5-m)
        res.append(grade)    
    return res
s = grading_student()
for i in s:
    print(i)
