
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('guess was (%s)'  % (guess))

toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('toss was (%s)'  % (toss))

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    logging.debug('guess[s] was (%s)'  % (guesss))
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')


logging.debug('End of program')