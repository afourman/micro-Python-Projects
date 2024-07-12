# Solution for https://www.geeksforgeeks.org/number-guessing-game-in-python/
#  Version using try/except
import random
import math

exec_seq = ('e', 'exit', 'E', 'Exit', 'q', 'Q')


def start():
    print(f'Welcome!')
    print(f'To quit game please enter one of follow:')
    print('|'.join(exec_seq))
    a = b = 0
    while True:
        get_input = input(f'Enter 2 different positive integer numbers to set range: ')
        if get_input in exec_seq:
            exit(f'Thank you')
        try:
            a, b = sorted(int(i) for i in set(get_input.split()))
            break
        except ValueError:
            print(f'Please, try again')
            continue
    print(f'Choosing number in range: {a} - {b} ...')
    return random.randint(a, b), math.ceil(math.log2(b - a + 1))


def game():
    number, guesses_count = start()
    tries = 1
    while guesses_count > 0:
        print(f'You have {guesses_count} attempts left')
        inp = input(f'Please enter number that you guess: ')
        if inp in exec_seq:
            exit(f'Thank you')
        try:
            num = int(inp)
        except ValueError:
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
    rep = input(f'Play again (yes or y)?')
    if rep.lower() == 'y' or rep.lower() == 'yes':
        game()
    exit(f'Sure, Thank you')


game()
