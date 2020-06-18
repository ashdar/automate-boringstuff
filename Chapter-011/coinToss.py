
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

# logging.disable(logging.DEBUG)
# logging.disable(logging.INFO)
# logging.disable(logging.WARNING)
# logging.disable(logging.ERROR)
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')


def translate_GuessStringToInteger(guess):

    if guess == 'heads':
        guessInteger = 1
    elif guess == 'tails':
        guessInteger = 0
    else:
        guessInteger = -1

    return guessInteger


import random

toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('toss was (%s)'  % (toss))

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

logging.debug('First guess was (%s)'  % (guess))

guessInteger = translate_GuessStringToInteger(guess)

if toss == guessInteger:
    print('You got it!')
    logging.info('You got it!')
else:
    print('Nope! Guess again!')
    logging.warning('Nope! Guess again!')

    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    
    logging.debug('Second guess was (%s)'  % (guess))

    guessInteger = translate_GuessStringToInteger(guess)

    if toss == guessInteger:
        print('You got it!')
        logging.info('You got it!')
    else:
        print('Nope. You are really bad at this game.')
        logging.warning('Nope! You are really bad at this game.')


logging.debug('End of program')