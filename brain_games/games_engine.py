#! /usr/bin/env python

import prompt


def play(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.GAME_RULE)
    max_rounds = 3
    for round in range(max_rounds):
        question, correct_answer = game.get_question_and_solution()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer != correct_answer:
            print(
                f'"{user_answer}" is wrong anwer ;(. Correct answer was'
                f' "{correct_answer}".\nLet\'s try again, {user_name}!'
            )
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {user_name}!')
