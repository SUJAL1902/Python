'''
WAP to create dictionary containing user details , access each
details manually using keys &amp; via loop?
'''

n = int(input("Enter number of key value pair : "))
dict1 = {}
for i in range(n):
    k = input(f"Enter {i+1} key :")
    v = input(f"Enter {i+1} value :")
    dict1[k]=v

print(dict1)

