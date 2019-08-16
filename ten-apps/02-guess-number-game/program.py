# App 2 guess number game
import random;


def header():
    print('===============================')
    print('===== Guess the Correct Integer!')
    print('===============================')


def game():
    num = random.randint(1, 100); # requires a range
    tries = 1
    playing = True
    guesses = []
    print('Guess a integer between 1 and 100')

    while playing:
        guess = input(': ')
        try:
            guessed_num = int(guess)
        except:
            print('You must enter an integer between 1 and 100')
            continue

        guesses.append(guessed_num)
        if guessed_num < num:
            print('{} is too low!!'.format(guessed_num))
            tries += 1
            continue
        elif guessed_num > num:
            print('{} is too high!!'.format(guessed_num))
            tries +=1
            continue
        else:
            print('Awesome! It took you {} guesses to correctly guess the winning integer.'.format(tries))
            print('You guessed {}'.format(str(guesses)))

            playing = False # end game loop
            print('') # print an empty line

            play_again = input('Would you like to play again? [Y]es or [N]o?')

            if play_again.upper() == 'Y':
                game()
            else:
                print('Thanks for playing! Goodbye')


def main():
    header()
    game()


if __name__ == '__main__':
    main()
