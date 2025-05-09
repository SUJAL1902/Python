'''
WAP to sort elements of 8 element list in descending order ,
without using builtin method?
'''

x = [1,2,3,4,5,6,7,8]
temp = 0
for i in range (0 , len(x) ,1) :
    for j in range (i + 1 , len(x),1) :
        if x[i] < x[j] :
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
print(x)