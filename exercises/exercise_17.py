# Your solution to Exercise 17

def lucky_ticket(str_num):
    sum1 = int(str_num[0]) + int(str_num[1]) + int(str_num[2]) 
    sum2 = int(str_num[3]) + int(str_num[4]) + int(str_num[5]) 
    return "Happy" if sum1 == sum2 else "Ordinary"

ticket = input()
print(lucky_ticket(ticket))