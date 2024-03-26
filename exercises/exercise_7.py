# Your solution to Exercise 7

def calc(op1, op2, operand):
    return str(op1 + op2) if operand == "+" else str(op1 - op2) if operand == "-" else str(op1 * op2) if operand == "*" else str(op1 % op2) if operand == "mod" else str(op1 ** op2) if operand == "pow" else str(op1 // op2) if operand == "div" and op2 != 0 else str(op1 / op2) if operand == "/" and op2 != 0 else "Division by 0!"

    
num1 = float(input())
num2 = float(input())
op = str(input())

print(calc(num1, num2, op))