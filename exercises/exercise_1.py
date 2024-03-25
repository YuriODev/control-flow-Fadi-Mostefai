# Your solution to Exercise 1

def age(A, T):
  return "Alex is the eldest." if A > T else "Tatyana is the eldest." if T > A else "Alex and Tatyana are of the same age."

A = int(input())
T = int(input())
print(age(A, T))