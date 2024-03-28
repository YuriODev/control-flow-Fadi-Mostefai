# Your solution to Exercise 11

def leap(year):
    if year % 4 == 0: 
        if year % 100 != 0:
            return "Leap year."
        elif year % 400 == 0:
            return "Leap year."
        else:
            return "Ordinary year."      
    else:
        return "Ordinary year."
    
yr = int(input())
print(leap(yr))