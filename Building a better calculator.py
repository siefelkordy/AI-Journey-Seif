def calc(num1,oper,num2):
    if oper == "+":
        return num1 + num2
    elif oper == "-":
        return num1 - num2
    elif oper == "*":
        return num1 * num2
    elif oper == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        print("Invalid operator")
        return None
    
num1 = float(input("Enter first number: "))
oper = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
result = calc(num1, oper, num2)
print("Result:", result)

    