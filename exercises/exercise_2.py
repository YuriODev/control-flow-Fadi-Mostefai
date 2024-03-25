# Your solution to Exercise 2

def stage(a):
  if 0 < a < 1:
    return "You are an infant."
  elif 1 < a < 13:
    return "You are a child."
  elif 13 < a < 20:
    return "You are a teenager."
  else:
    return "You are an adult."

age = int(input())
print(stage(age))