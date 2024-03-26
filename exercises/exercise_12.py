# Your solution to Exercise 12

def replace(num):
    str_num = str(num)
    str_num[0] = "*" if int(str_num[0]) % 2 == 0 else str_num[0]
    str_num[1] = "*" if int(str_num[1]) % 2 == 0 else str_num[1]
    str_num[2] = "*" if int(str_num[2]) % 2 == 0 else str_num[2]
    str_num[3] = "*" if int(str_num[3]) % 2 == 0 else str_num[3]
    return str_num

num = int(input())
print(replace(num))
