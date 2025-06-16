def cube(number):
    """Returns the cube of a number."""
    return number * number * number

def square(number):
    """Returns the square of a number."""
    return number ** 2  

num = int(input("Enter a number: "))
result = cube(num)
print(result)
