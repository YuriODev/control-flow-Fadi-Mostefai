# Your solution to Exercise 10

def is90(Ax, Ay, Bx, By, Cx, Cy):
    if Ax == Ay == Bx == By == Cx == Cy == 0:
        return "No"
    else:
        len_a = ((Bx - Ax) ** 2) + ((By - Ay) ** 2) # 9
        len_b = ((Cx - Bx) ** 2) + ((Cy - By) ** 2) # 9
        len_c = ((Ax - Cx) ** 2) + ((Ay - Cy) ** 2) # 18
        if len_a == len_b + len_c or len_b == len_c + len_a or len_c == len_b + len_a:
            return "Yes"
        else:
            return "No"
    
Ax = int(input()) # 1
Ay = int(input()) # 1
Bx = int(input()) # 1
By = int(input()) # 4
Cx = int(input()) # 4
Cy = int(input()) # 4

print(is90(Ax, Ay, Bx, By, Cx, Cy))