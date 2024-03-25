# Your solution to Exercise 6

def distance(Ax, Ay, Bx, By):
    return "A is further from the origin." if (((Ax ** 2) + (Ay ** 2)) ** 0.5) > (((Bx ** 2) + (By ** 2)) ** 0.5) else "B is further from the origin." if (((Bx ** 2) + (By ** 2)) ** 0.5) > (((Ax ** 2) + (Ay ** 2)) ** 0.5) else "A and B are at the same distance from the origin."

Ax = int(input())
Ay = int(input())
Bx = int(input())
By = int(input())

print(distance(Ax, Ay, Bx, By))