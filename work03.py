import csv

f = open("occupations.csv", "r")
csvfile = f.read()
csvfile = csvfile.split("\r\n")
csvfile = csvfile[1:-2]

f.close()

dictionary = {}

for line in csvfile:
    innerdict = line.split(",")
    #print innerdict
    dictionary[innerdict[0]] = innerdict[1]

#print csvfile[0]
print dictionary


"""
with open("occupations.csv","r") as csvfile:
    for row in csvfile:
        print row
"""
