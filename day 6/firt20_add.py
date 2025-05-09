'''
WAP to add all elements of list containing first 20 natural
number?
'''
list = []
sum = 0
for i in range (0 , 20) :
    list.insert(i , i + 1)

for i in range (len(list)) :
    sum += i
print(sum)