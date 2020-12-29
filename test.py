#output the highest score in the class
student_scores = input("Input a list of student scores \n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

'''
#input: 78 65 89 86 55 91 64 89
max_score = max(student_scores)
min_score = min(student_scores)
'''


#to loop for the highest score from the input
max_score = 0
for score in student_scores:
  if score > max_score:
    max_score = score


#to loop for the lowest score from the input
min_score = 100
for score in student_scores:
  if score < min_score:
    min_score = score

#will output the result here
print(f"Max score is: {max_score}")
print(f"Min score is: {min_score}")