import random
import time

while True:
    print('1. Roll the Dice.\n2. Exit\n')
    a = int(input('Enter your choice: '))
    if a == 1:
        print('Dice is rolling ....')
        time.sleep(1)
        num = random.randint(1,6)
        print('Result: {}'.format(num))
    else:
        print('Exiting ....')
        break
