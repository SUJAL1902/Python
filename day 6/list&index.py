'''
WAP to create list containing 10 elements , access each
elements of list by index &amp; loop?
'''

x = []
for i in range (10) :
    x.append(input())
for i in range (len(x)) :
    print(' At index',i, 'the value is ',x[i])