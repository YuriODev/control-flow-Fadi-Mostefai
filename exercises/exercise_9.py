# Your solution to Exercise 9

def comp(num):
    str_num = str(num)
    sum = int(str_num[0]) + int(str_num[2])
    return ">" if sum > int(str_num[1]) else "<" if sum < int(str_num[1]) else "="

num = int(input())
print(comp(num))