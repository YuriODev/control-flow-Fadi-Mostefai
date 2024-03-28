# Your solution to Exercise 2

def stage(a):
  return "You are an infant." if 0 < a <= 1 else "You are a child." if 1 < a < 13 else "You are a teenager." if 13 <= a < 20 else "You are an adult."

age = int(input())
print(stage(age))