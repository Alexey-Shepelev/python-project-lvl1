#! /usr/bin/env python

from random import randint


game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_solution():
    question = randint(1, 1000)

    if question < 2:
        correct_answer = 'no'

    elif question == 2:
        correct_answer = 'yes'

    i = 2
    while i <= question ** (1 / 2):
        if question % i == 0:
            correct_answer = 'no'
            break
        else:
            i += 1
            correct_answer = 'yes'

    return (question, correct_answer)
