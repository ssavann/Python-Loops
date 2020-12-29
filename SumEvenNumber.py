#Will do the sum of all Even number from 1 to 100

sumEvenNumber = 0

for number in range(1, 101):
	if number % 2 == 0:
		sumEvenNumber += number
		print(sumEvenNumber)

print(f"The sum of Even numbers is: {sumEvenNumber}")
