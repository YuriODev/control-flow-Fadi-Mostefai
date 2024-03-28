# Your solution to Exercise 15

def convert(day, month, year):
    if month != 2:
        if month < 8:
            if month % 2 != 0:
                if day == 31:
                    day = 1
                    month += 1
                else:
                    day += 1
            else:
                if day == 30:
                    day = 1
                    month += 1
                else:
                    day += 1
        else:
            if month % 2 != 0:
                if day == 30:
                    day = 1
                    month += 1
                else:
                    day += 1
            elif month % 2 == 0 and month != 12:
                if day == 31:
                    day = 1
                    month += 1
                else:
                    day += 1
            else:
                if day == 31:
                    day = 1
                    month = 1
                    year += 1
                else:
                    day += 1
    else:
        if year % 4 == 0:
            if day == 29:
                day = 1
                month += 1
            else:
                day += 1
        else:
            if day == 28:
                day = 1
                month += 1
            else:
                day += 1
    return f"{day}.{month}.{year}"

day = int(input())
month = int(input())
year = int(input())
print(convert(day, month, year))