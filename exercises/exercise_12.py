# Your solution to Exercise 12

def replace(num):
    str_num = str(num)
    new_num = ""
    new_num += "*" if int(str_num[0]) % 2 == 0 else str_num[0]
    new_num += "*" if int(str_num[1]) % 2 == 0 else str_num[1]
    new_num += "*" if int(str_num[2]) % 2 == 0 else str_num[2]
    new_num += "*" if int(str_num[3]) % 2 == 0 else str_num[3]
    return new_num

num = int(input())
print(replace(num))
