import csv
import findpeer
import sys

def csvread(pp,rec,csvfile='data.csv'):
	reader = csv.reader(open(csvfile,'r'))
	for line in reader:
		if line[0]=='':
			for letter in line[1:]:
				pp.append(letter)
		else:
			rec.append(line[1:])

#main
people=[]
record=[]
csvread(people,record)

if len(people)%2:
	people.append("NULL")
	for line in record:
		line.append("")
	
	tmp = []
	for i in range(0,len(people)):
		tmp.append("")
	record.append(tmp)

for i in range(len(people)):
    for j in range(len(people)):
        if record[i][j] == "":
            record[i][j] = 0
        else:
            record[i][j] = int(record[i][j])

#print people
#print record
fp = findpeer.FindPeer()
fp.MM(len(people))
#print fp.possiblecomb
fp.getcombkv(record)
fp.findmaxpeercomb(people)
#fp.findmaxpeer(candidate,people,record)
