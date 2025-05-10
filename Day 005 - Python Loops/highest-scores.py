student_scores = [150,142,185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]

total_exam_scores = sum(student_scores)
print(total_exam_scores)

sum = 0
for score in student_scores :
    sum += score
print(sum)

max = 0
for score in student_scores :
    if max < score:
        max = score
    else:
        max = max
print(max)