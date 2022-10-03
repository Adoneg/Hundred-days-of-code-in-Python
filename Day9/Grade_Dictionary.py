from re import S


student_scores = {
    "Harry" : 81,
    "Ako" : 78,
    "Ado" : 99,
    "Anji" : 74,
    "Nervis" : 62,
}

student_grade = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grade[student] = "Outstanding"
    elif score > 80:
        student_grade[student] = "Exceeds Expectations"
    elif score > 70:
        student_grade[student] = "Acceptable"
    else:
        student_scores[student] = "Failed"

        
print(student_grade)