from random import randint
from IPython.display import clear_output

guessed = False
number = randint(0,100)
guess = 0

while not guessed:
    ans = input('Please enter a guess: ')

    guess += 1

    clear_output()

    if int(ans) == number:
        print('Congrats! You guessed it correctly. ')
        print('It took you {} guess!' .format(guess))
        break
    elif int(ans) > number:
        print('The number is lower than what you guessed.Please try again.. ')
    elif int(ans) < number:
        print('The number is greater than what you guessed.Please try again.. ')