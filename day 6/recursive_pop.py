'''
WAP to remove recursive occuring elements
input list : [1,2,1,1,3,3,2,2,4,4,5,6,6,5,7,7,8,9,9]
output list : [1,2,3,4,5,6,7,8,9]
'''

x = [1,2,1,1,3,3,2,2,4,4,5,6,6,5,7,7,8,9,9]
y = []
for i in range (len(x)) :
    if x[i] in y:
        continue
    else:
        y.append(x[i])
print(y)