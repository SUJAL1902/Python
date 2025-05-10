'''
Multiply All Items in a Dictionary
'''
d = {'value1': 5,'value2': 4,'value3': 3,'value4': 2,'value5': 1,}

answer = 1

for i in d:
	answer = answer*d[i]
print(answer)
