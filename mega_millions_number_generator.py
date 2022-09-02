# Create a number generator for Mega Millions Lottery tickets.

import random
tickets = 0

req_tickets = int(input("How many tickets will you purchase? "))

white_numbers = []
mega_ball = []
while tickets < req_tickets:
    # generate 5 random numbers between 1-70 for each ticket
    for white_num in range(1, 5 + 1):
        num_selection = random.randint(1, 70)
        # checks for duplicate values, re-runs generator if found, otherwise, appends to list
        if num_selection in white_numbers:
            num_selection = random.randint(1, 70)
        else:   
            white_numbers.append(num_selection)
    # generate 1 random number between 1-25 for each ticket
    for mega_num in range(req_tickets):
        mega_selection = random.randint(1,25)
        mega_ball.append(mega_selection)
    print(*white_numbers, f"({mega_ball[0]})")
    # deletes all values in the list each cycle
    del white_numbers[:]
    del mega_ball[:]
    # increments # of tickets each cycle until loop condition met
    tickets += 1

