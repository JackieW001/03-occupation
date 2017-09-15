import csv
import random
dictionary = {}
lit = []

def future_occupation():
	with open("occupations.csv", "r") as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			dictionary[row[0]] = row[1]
	
	del dictionary["Job Class"]
	del dictionary["Total"]
	for i in dictionary:
		num = 0
		while num < (float(dictionary[i])*10):
			lit.append(i)
			num += 1
		
	return random.choice(lit)

print future_occupation()
