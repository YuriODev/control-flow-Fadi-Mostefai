# Your solution to Exercise 5

def roots(a, b, c):
    discriminant = ((b ** 2) - (4 * a * c))
    if a == b == c == 0:
        return "Infinite roots."
    elif a != 0:
        if discriminant > 0:
            root1 = (-b + (discriminant ** 0.5)) / (2 * a)
            root2 = (-b - (discriminant ** 0.5)) / (2 * a)
            return f"{root1} and {root2}"
        elif discriminant == 0:
            root1 = (-b) / (2 * a)
            return str(root1)
        else:
            return "No roots."
    else:
        if b != 0:
            if c != 0:
                root1 = (-c) / b
                return str(root1)
            else:
                root1 = 0
                return str(root1)
        else:
            return "No roots."
    
a = float(input())
b = float(input())
c = float(input())

print(roots(a,b,c))    
