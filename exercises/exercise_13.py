# Your solution to Exercise 13

def diff(num):
    str_num =str(num)
    return True if len(set(str_num)) == len(str_num) else False

num = int(input())
print(diff(num))