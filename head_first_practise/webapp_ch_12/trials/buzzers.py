
from datetime import datetime
from pprint import pprint

def convert2ampm(time24:str)->str:
	return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

print('\n')

with open('buzzers.csv') as data:
	ignore = data.readline()
	flights1 = {}
	for line in data:
		time,destination = line.strip().split(',')
		flights1[time] = destination
pprint(flights1)

print('\n')

flights2={}
for time,destination in flights1.items():
	flights2[convert2ampm(time)] = destination.title()
pprint(flights2)

print('\n')

when = {}
for dest in set(flights2.values()):
	when[dest] = [time for time,destination in flights2.items() if destination == dest]
pprint(when)



