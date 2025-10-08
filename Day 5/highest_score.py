student_scores = [158, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_scores = sum(student_scores)
print(total_exam_scores)

sum = 0
for score in student_scores:
    sum += score

print(sum)

print(max(student_scores)) # Prints the greater score on the list


bigger = 0

for score in student_scores:
    if score > bigger:
        bigger = score

print(bigger)