# Create a number generator for Mega Millions Lottery tickets.
# Requirements:  
# 5 "white" numbers valued between 1-70
# 1 "mega ball" number valued between 1-25
# Provide randomly generated numbers for the number of tickets submitted by user input
# Print out tickets

import random
tickets = 0
req_tickets = int(input("How many tickets will you purchase? "))
white_numbers = []
mega_ball = []
while tickets < req_tickets:
    for white_num in range(1, 5 + 1):
        num_selection = random.randint(1, 70)
        white_numbers.append(num_selection)
    for mega_num in range(req_tickets - 1):
        mega_selection = random.randint(1,25)
        mega_ball.append(mega_selection)
    print(*white_numbers, f"({mega_ball[0]})")
    del white_numbers[:]
    del mega_ball[:]
    tickets += 1



