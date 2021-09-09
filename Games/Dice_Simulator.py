# This program simulates the rolling of a 6 sides dice

import random

rolling = True

while rolling:
    # Create a random number from 1 to 6.
    dice = random.randint(1, 6)
    print("Press Enter to roll or q to Quit.")
    start = input(">>")

    # Keeps rolling until user enters a q to quit.
    if start.lower() != "q":
        print("You rolled a", dice)
    else:
        rolling = False
print("Thank for Playing!!")
