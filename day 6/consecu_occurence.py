'''
WAP to remove consicutive occuring elements
input list : [1,2,1,1,3,3,2,2,4,4,5,6,6,5,7,7,8,9,9]
output list : [1,2,1,3,2,4,5,6,5,7,8,9]
'''

x = [1,2,1,1,3,3,2,2,4,4,5,6,6,5,7,7,8,9,9]

for i in range (1,len(x),1) :
    if x[i] == x[i-1]:
        x.remove(x[i-1])
print(x)








#     if x[i] == x[i-1] :
#         x.remove(x[i])
# print(x)