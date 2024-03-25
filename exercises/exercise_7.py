# Your solution to Exercise 7

def calc(op1, op2, operand):
    if operand == "+":
        return str(op1 + op2)
    elif operand == "-":
        return str(op1 - op2)
    elif operand == "*":
        return str(op1 * op2)
    elif operand == "/":
        if op2 != 0:
            return str(op1 / op2)
        else:
            return "Division by 0!"
    elif operand == "mod":
        return str(op1 % op2)
    elif operand == "pow":
        return str(op1 ** op2)
    elif operand == "div":
        return str(op1 // op2)
    
num1 = float(input())
num2 = float(input())
op = str(input())

print(calc(num1, num2, op))