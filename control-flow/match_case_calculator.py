"""
A simple calculator that prompts user to enter two operands and the 
selects an operation.
"""
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation ( +, -, *, /): ")

match operation:
    case "+":
        print("The result is " + str(num1 + num2) + ".")
    case "-":
        print("The result is " + str(num1 - num2) + ".")
    case "*":
        print("The result is " + str(num1 * num2) + ".")
    case "/":  
        print("The result is " + str(num1 / num2) + ".") if num2 != 0 \
        else print("Cannot divide by zero.")
