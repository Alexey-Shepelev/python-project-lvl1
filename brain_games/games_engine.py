#! /usr/bin/env python

import prompt


def play_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.game_rule)
    end_game_msg = (f'Congratulations, {user_name}!')
    i = 0
    for i in range(3):
        question, correct_answer = game.get_question_and_solution()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            end_game_msg = (
                f'"{user_answer}" is wrong anwer ;(. Correct answer was'
                f' "{correct_answer}".\nLet\'s try again, {user_name}!'
            )
            break
    print(end_game_msg)
