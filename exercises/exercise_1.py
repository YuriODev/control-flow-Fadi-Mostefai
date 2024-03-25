# Your solution to Exercise 1

def age(A, T):
  if A > T:
    return "Alex is the eldest."
  elif A < T:
    return "Tatyana is the eldest."
  else:
    return "Alex and Tatyana are of the same age."

A = int(input())
T = int(input())
print(age(A, T))