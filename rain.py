# This is a python program that displays falling raindrops

import time
import random


# Config
WIDTH = int(input("Enter width: "))
HEIGHT = int(input("Enter height: "))
DELAY = float(input("Enter delay (Recommended -> 0.05): "))
CHANCE_MULTIPLIER = float(input("Raindrop chance multiplier (Recommended -> 0.01): "))
WIND = int(input("Enter wind direction (+-0): "))
INVERSE = bool(input("Inverse? (True, False): "))
RAIN = ['|']
SPLASH= ['-']
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

    # Splash
    for i, char in enumerate(box[0]):
        if char in RAIN:
            box[0][i] = random.choice(SPLASH)
    
    # Wind
    for i, y in enumerate(box):
        if WIND>0:
            for _ in range(abs(WIND)):
                box[i].insert(0, EMPTY)
                del box[i][WIDTH]

        elif WIND<0:
            for _ in range(abs(WIND)):
                box[i].append(EMPTY)
                del box[i][0]


# Loop
while True:
    populate()
    display()
    time.sleep(DELAY)




