'''
WAP to check a number is armstrong or not using function
without argument &amp; with return value
'''
def is_armstrong():
    num = int(input("Enter a number: "))
    original_num = num
    num_digits = len(str(num))

    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** num_digits
        num = num // 10  

    if original_num == total:
        return True
    else:
        return False

result = is_armstrong()

if result:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
