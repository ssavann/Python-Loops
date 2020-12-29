student_heights = input("Input a list of student heights with space\n").split()   
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


'''
#without the "for" loop
total_height = sum(student_heights)
number_of_students = len(student_heights)
average =  round(total_height / number_of_students)
'''



#will make a sum of all the height
#enter: 180 124 165 173 188 144 157
total_height = 0
for height in student_heights:
  total_height += height
# print(total_height)     # the sum is: 1131


#will count the number of students in the list
number_of_students = 0
for student in student_heights:
  number_of_students += 1
# print(number_of_students)

#will make an average by dividing "total_height" by "number_of_students"
average =  round(total_height / number_of_students)
print(f"Student height average is: {average} cm" )

