# Your solution to Exercise 16
# Your solution to Exercise 15

def convert(day, month, year):
    if month != 3:
        if month < 8:
            if month % 2 != 0 and month != 1:
                if day == 1:
                    day = 30
                    month -= 1
                else:
                    day -= 1
            elif month % 2 == 0:
                if day == 1:
                    day = 31
                    month -= 1
                else:
                    day -= 1
            else:
                if day == 1:
                    day = 31
                    month = 12
                    year -= 1
                else:
                    day -= 1
        else:
            if month % 2 != 0:
                if day == 1:
                    day = 31
                    month -= 1
                else:
                    day -= 1
            elif month % 2 == 0 and month != 8:
                if day == 1:
                    day = 30
                    month -= 1
                else:
                    day -= 1
            else:
                if day == 1:
                    day = 31
                    month -= 1
                else:
                    day -= 1
    else:
        if year % 4 == 0:
            if day == 1:
                day = 29
                month -= 1
            else:
                day -= 1
        else:
            if day == 1:
                day = 28
                month -= 1
            else:
                day -= 1
    return f"0{day}.0{month}.{year}" if month < 10 and day < 10 else f"{day}.0{month}.{year}" if month < 10 else f"0{day}.{month}.{year}" if day < 10 else f"{day}.{month}.{year}"

day = int(input())
month = int(input())
year = int(input())
print(convert(day, month, year))