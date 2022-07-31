# This is a python program that displays animated rain

import time
import random


# Config
WIDTH = int(input("Enter width: "))
HEIGHT = int(input("Enter height: "))
DELAY = float(input("Enter delay: "))
CHANCE_MULTIPLIER = float(input("Raindrop chance multiplier (Recommended -> 0.01): "))
INVERSE = bool(input("Inverse? (True, False): "))
RAIN = ['*']
EMPTY = " "

# Initialize box
box = []
for y in range(HEIGHT):
    box.append([EMPTY for i in range(WIDTH)])



# Funcs
def display():
    screen = box

    # Inverse
    if INVERSE:
        screen = reversed(box)

    # To string
    out = ""
    for y in screen:
        for char in y:
            out += char

        out += "\n"
    
    print(out)


def populate():
    for i, y in enumerate(box):
        if i != len(box)-1:
            box[i] = box[i+1]

    
    box[len(box)-1] = [EMPTY for i in range(WIDTH)]
    
    # Randomizer

    for i, char in enumerate(box[len(box)-1]):
        if random.randint(0,100) <= 100*CHANCE_MULTIPLIER:
            box[len(box)-1][i] = random.choice(RAIN)



# Loop
while True:
    populate()
    display()
    time.sleep(DELAY)




