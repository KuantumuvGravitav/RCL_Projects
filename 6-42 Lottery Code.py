from random import randint
from functools import reduce

lottery = []
new_number = 0
my_numbers = []
win = 0

while len(lottery) < 6:
    new_number = randint(1, 42)

    if new_number not in lottery:
        lottery.append(new_number)

while len(my_numbers) < 6:
    try:
        new_number = int(input('Please pick your number from 1 to 42: '))
    except ValueError:
        print()
        print('Invalid input!')
        quit()

    if new_number in my_numbers:
        print()
        print('Please enter a unique number.')
        quit()
    elif new_number > 42 or new_number < 1:
        print()
        print('Please enter a unique number.')
        quit()
    else:
        my_numbers.append(new_number)

win = reduce(lambda x, y: x + lottery.count(y), set(my_numbers), 0)
if win == 6:
    print('Congratulations! You hit the jackpot!')
    print('Your numbers are', my_numbers)
    print('The lucky numbers are', lottery)
elif win == 3 or win == 4 or win == 5:
    print()
    print('Your numbers are', my_numbers)
    print('The lucky numbers are', lottery)
    print(f'You have won {win} numbers!')
else:
    print()
    print('You lose.')
    print('The lucky numbers are', lottery)