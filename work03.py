import csv

f = open("occupations.csv", "r")
csvfile = f.read()
csvfile = csvfile.split("\r\n")
csvfile = csvfile[1:-2]

print csvfile
f.close()


"""
with open("occupations.csv","r") as csvfile:
    for row in csvfile:
        print row
"""
