'''
Write a Python program to map two lists into a dictionary.
'''

a = ["name", "age", "city"]
b = ["Alice", 30, "New York"]

res = dict(zip(a, b))
print(res)