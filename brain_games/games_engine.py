#! /usr/bin/env python

import prompt


def main_engine(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.game_rule)
    game_over_msg = (f'Congratulations, {user_name}!')
    i = 0
    while i < 3:
        question, correct_answer = game.get_question_and_solution()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            i = 3
            game_over_msg = (
                f'"{user_answer}" is wrong anwer ;(. Correct answer was'
                f' "{correct_answer}".\nLet\'s try again, {user_name}!'
            )
    print(game_over_msg)
