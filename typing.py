'''
Typing practice. Useful if you have a programmable keyboard
and want to establish muscle memory after remapping keys

@author: Russ Winch
@version: Jan 2018
'''

import random
import curses

''' executes a round of practice '''
def practice(w, k, r, m):
    w.addstr("\t{message}\nround {round_no}.\t{key} : ".format(message=m,
        round_no=r, key=k))
    result = w.getkey()

    if result == k:
        return True
    return False


''' selects a new key from the pool '''
def new_key(l):
    return l[random.randrange(len(l))]


def main():
    rounds_default = 10

    keys = None
    while not keys:
        keys = list(str(input("which keys to practice? : ")))

    rounds = input("how many rounds? (default={}):".format(rounds_default))
    if not rounds:
        rounds = rounds_default
    else:
        try:
            rounds = int(rounds)
        except:
            rounds = rounds_default

    # initialise
    message = ''
    current_key = new_key(keys)
    current_round = 1
    incorrect = 0

    # time to practice!
    try:
        win = curses.initscr()
        # next 2 lines allow scrolling, otherwise an error occurs
        win.scrollok(True)
        win.idlok(1)
        win.addstr("let's practice {keys} for {rounds} rounds".format(keys=keys,
            rounds=rounds))

        while current_round <= rounds:
            if practice(win, current_key, current_round, message):
                current_key = new_key(keys)
                current_round += 1
                message = 'correct!'
            else:
                message = 'incorrect! try again'
                incorrect += 1
    except:
        raise
    finally:
        curses.endwin() # without this bad things happen to the terminal

    # results
    if incorrect == 1:
        s = ''
    else:
        s = 's'
    print("you made {i} mistake{s}".format(i=incorrect, s=s))


if __name__ == "__main__":
    main()
