import csv
import findpeer

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

fp = findpeer.FindPeer()
candidate = fp.MM(len(people))
fp.findmaxpeer(candidate,people,record)