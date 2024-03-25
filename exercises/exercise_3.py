# Your solution to Exercise 3

def rhoulette(num):
  if num == 0:
    return "Green"
  elif 1 <= num <= 10:
    return "Black" if num % 2 == 0 else "Red"
  elif 11 <= num <= 18:
    return "Red" if num % 2 == 0 else "Black"
  elif 19 <= num <= 28:
    return "Black" if num % 2 == 0 else "Red"
  elif 29 <= num <= 36:
    return "Red" if num % 2 == 0 else "Black"
  else:
    return "The bet will not play!"
  
num = int(input())
print(rhoulette(num))