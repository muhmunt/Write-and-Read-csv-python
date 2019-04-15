import csv

a = open('prasarana.csv','r')
reader = csv.reader(a)

#read
for row in reader:
    print (row)

#close
a.close()