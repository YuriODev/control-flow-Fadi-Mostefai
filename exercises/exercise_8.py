# Your solution to Exercise 8

def find(num, dig):
    return True if str(dig) in str(num) else False

num = int(input())
dig = int(input())
print(find(num, dig))