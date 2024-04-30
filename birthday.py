import time
from random import randint

def explode_heart():
    heart = [
        "  ❤️   ",
        " 💓💓  ",
        "💖💖💖 ",
        " 💓💓  ",
        "  ❤️   "
    ]
    for _ in range(3):
        for line in heart:
            print(line)
            time.sleep(0.1)
        print("\033[A\033[A\033[A\033[A\033[A") # Move cursor up 5 lines

for i in range(1, 85):
    print('')

space = ''
for i in range(1, 1000):
    count = randint(1, 100)
    while count > 0:
        space += ' '
        count -= 1
    if i % 10 == 0:
        print(space + '🎂Happy Birthday to the love of my life!')
    elif i % 9 == 0:
        print(space + "🎂")
    elif i % 5 == 0:
        print(space + "💛")
    elif i % 8 == 0:
        print(space + "🎉")
    elif i % 7 == 0:
        print(space + "🍫")
    elif i % 6 == 0:
        print(space + "Happy Birthday!💖")
    elif i % 13 == 0:
        explode_heart()
    else:
        print(space + "🔸")
    space = ''
    time.sleep(0.2)

print("\nI'm so happy to see your growth since we've been together! You've grown into the most amazing person, and I'm grateful to share this journey with you. Happy Birthday, my love!")
