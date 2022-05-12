student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

students = 0
totalScore = 0
highestScore = 0
for scores in student_scores:
    students += 1
print(f'The total of students is: {students}')

for score in student_scores:
    if score > highestScore:
        highestScore = score
print(f'The Highest score in the class is: {highestScore}')

for scores in student_scores:
    totalScore += scores
print (f'The total of test scores is: {totalScore}')

#--------------- ///
print("")
list = 101
for numbers in range(0, list, 3):
    total = numbers

for numbers in range(0, list, 3):
    total = 100 - numbers
    print(numbers,total)
print("")
print("")
totalTwo = 0
for numbers in range(1, list):
    if numbers % 2 == 0:
        totalTwo += numbers
print(totalTwo)
