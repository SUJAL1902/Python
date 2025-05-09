'''
Check Common Member Between Two Lists
'''
list = [1 ,2 ,3 ,4, 5, 6]

list1 = [9, 8 ,7 ,6 ,5 ,4 ]

for i in range (0 , len(list) , 1) :
    for j in range (0 , len(list1),1) :
        if list [i] == list1[j] :
            print(int(list[i]))
        