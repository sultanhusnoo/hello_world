
print("\n*********************************************************\n")

data1 = [1,2,3,4,5,6,7,8]
print("Here is the original data:",data1)
evens_for = []
for num in data1:
	if not num%2:
		evens_for.append(num)
print("Here is the even numbers using for loop:  ",evens_for)
evens_comp = [num for num in data1 if not num%2]		
print("Here is the even numbers using List Comp: ",evens_comp)

print("\n*********************************************************\n")

data2 = [1,'one',2,'two',3,'three',4,'four']
print("Here is the original data:",data2)
words_for = []
for num in data2:
	if isinstance(num,str):
		words_for.append(num)
print("Here is the data uing for loop:  ",words_for)
words_comp = [num for num in data2 if isinstance(num,str)]
print("Here is the data uing List Comp: ",words_comp)

print("\n*********************************************************\n")

data3 = list('So long and thanks for all the fish'.split())
print("Here is the original data: ", data3)
title_for=[]
for word in data3:
	title_for.append(word.title())
print("Here is the result using for loop:  ",title_for)
title_comp = [word.title() for word in data3]
print("Here is the result using List Comp: ",title_comp)

print("\n*********************************************************\n")
