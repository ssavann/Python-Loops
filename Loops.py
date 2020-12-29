#simple "for" loop

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
 	print(fruit)
 	print(fruit + " Pie")	#inside the same loop

print("=================")

#For Loop with "range": will print out -> 1 to 9 but not 10 
# will increase by 1 -> 1 + 1 = 2
for number in range(1, 10):	
	print(number)


print("=================")

#will output numbers from 1 to 20. will increase by 3 -> 1 + 3 = 4, 4 + 3 = 7
for number in range(1, 20, 3):	
	print(number)

print("=================")

total = 0
for number in range(1, 101):
	total += number
	print(total)

print(total)
