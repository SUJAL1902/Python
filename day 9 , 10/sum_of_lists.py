'''
Input data exactly in the following format, and print sum of all
integer values.
“67, 89, 23, 67, 12, 55, 66”.
'''

list1 = list(map(int, input("Enter integers separated by spaces: ").split()))
print(list1)

res = 0
for i in list1 :
    res += i

print("Sum of integer is : ", res)