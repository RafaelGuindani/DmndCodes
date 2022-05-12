student_heights = [180, 124, 165, 173, 189, 169, 146]
a = sum(student_heights)
b = len(student_heights)
c = int(a)/int(b)
print('The average height is',round(c))

# ----------------------- ///
totalHeight = 0
numberOfStudents = 0

for student in student_heights:
    numberOfStudents += 1
print(numberOfStudents)

for height in student_heights:
    totalHeight += height

averageHeight = round(totalHeight / numberOfStudents)
print(f'The average height is {averageHeight}')
