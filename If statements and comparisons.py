def max_num(num1, num2 ,num3):
    """Returns the maximum of two numbers."""
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")
num3 = input("Enter 3rd number: ")

print("The maximum number is:", max_num(num1,num2,num3))