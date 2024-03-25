# Your solution to Exercise 4

def grade(num):
    return "initial level" if 1 <= num <= 3 else "average level" if 4 <= num <= 6 else "sufficient level" if 7 <= num <= 9 else "high level" if 10 <= num <= 12 else "level is absent"

num = int(input())
print(grade(num))