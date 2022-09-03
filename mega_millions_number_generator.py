# Create a number generator for Mega Millions Lottery tickets.

import random
tickets = 0

while True:
    try:
        req_tickets = int(input("How many tickets will you purchase? "))
        if req_tickets < 1:
            raise ValueError
    except ValueError:
        print("Please select a numeric value of 1 or more.")
    else:
        break


white_numbers = list(range(1,71))
mega_ball = list(range(1,26))

while tickets < req_tickets:
    num_selection = random.shuffle(white_numbers)
    num_selection = random.shuffle(mega_ball)
    print(*white_numbers[0:5], f"({mega_ball[0]})")
    tickets += 1

