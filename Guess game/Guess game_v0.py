# Solution for https://www.geeksforgeeks.org/number-guessing-game-in-python/
#  Version using try/except
import random
import math


def start():
    print(f'Welcome!')
    print(f'To quit game please enter one of follow:')
    for i in ('e', 'exit', 'E', 'Exit', 'q', 'Q'):
        print(i, end=' | ')
    else:
        print()
    a = b = 0
    while True:
        get_input = (input('Enter 2 different positive integer numbers to set range: ').split())
        if get_input[0] in ('e', 'exit', 'E', 'Exit', 'q', 'Q'):
            exit('Thank you')
        if (len(get_input) == 2 and  # input validation
               (get_input[0].isnumeric()) and
                (get_input[1].isnumeric())):
            a, b = sorted((int(get_input[0]), int(get_input[1])))
            break
        else:
            print(f'Please, try again')
            continue
    print(f'Choosing number in range: {a} - {b} ...')
    return random.randint(a, b), math.ceil(math.log2(b-a+1))


def game():
    number, guesses_count = start()
    tries = 1
    while guesses_count > 0:
        print(f'You have {guesses_count} attempts left')
        inp = input('Please enter number that you guess: ').split()
        if inp[0] in ('e', 'exit', 'E', 'Exit', 'q', 'Q'):
            exit('Thank you')
        if (len(inp) == 1 and  # input validation
                (inp[0].isnumeric())):
            num = int(inp[0])
        else:
            continue
        guesses_count -= 1
        if num == number:
            print(f'YOU WON!\n(ON {tries} TRY)\n{num} is a chosen number!')
            break
        elif (num != number) and (guesses_count == 0):
            print(f'You lose! Chosen number was {number}')
            break
        elif num > number:
            print(f'Your number too high')
        else:
            print(f'Your number too low')
        tries += 1


game()
