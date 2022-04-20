#! /usr/bin/env python

from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, oterwise answer "no".')
    game_over_msg = (f'Congratulations, {user_name}!')
    i = 0
    while i < 3:
        random_number = randint(1, 99)
        print(f'Question: {random_number}')
        user_answer = input('Your answer: ')
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        if user_answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            i = 3 
            game_over_msg = (f'"{user_answer}" is wrong anwer ;(. Correct answer was "{correct_answer}".\nLet\'s try again {user_name}!')
    print(game_over_msg)


if __name__ == '__main__':
    main()