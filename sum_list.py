student_score = [78, 65, 89, 86, 55, 91, 64, 89,99, 100 ,74,88]

# finding the sum of all number in the list:
sum = 0
for score in student_score:
    print(score)
    sum += score
print(sum)


# finding the sum of all number from 1 to 100 in the list:
total = 0
for i in range(1,101):
    total += i
print(total)


# finding the max number in the list 
max = student_score[0]
for i in range(len(student_score)):
    if student_score[i] > max:
        max = student_score[i]
print("The highest score in the class is:", max)


# finding the lowest number in the list
min = student_score[0]
for i in range(len(student_score)):
    if student_score[i] < min:
        min = student_score[i]
print("The lowest score in the class is:", min)


