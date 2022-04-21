#! /usr/bin/env python

from random import randint


game_rule = 'Answer "yes" if the number is even, oterwise answer "no".'


def get_question_and_solution():
    question = randint(1, 99)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return (question, correct_answer)
