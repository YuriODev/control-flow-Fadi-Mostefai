# Your solution to Exercise 14

def palindrome(num):
    str_num = str(num)
    print(str_num[::2])
    print(str_num[2::][::-1])
    return True if str_num[::2] == str_num[2::][::-1] else False

num = int(input())
print(palindrome(num))