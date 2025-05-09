'''
WAP to search element inside list?
'''

list = [1,2,6,8,5,3,7,4]

x = int(input( 'enter the target : '))
for i in range (0,len(list),1) :
    if list[i] == int(x) :
        print(' The target is at index ',i)