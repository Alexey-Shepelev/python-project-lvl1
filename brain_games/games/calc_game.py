#! /usr/bin/env python

from random import randint, choice


GAME_RULE = 'What is the result of the expression?'


def get_question_and_solution():
    member_1 = randint(1, 20)
    member_2 = randint(1, 20)
    operators = ('+', '-', '*')
    operator = choice(operators)
    if operator == '+':
        expression = member_1 + member_2
    elif operator == '-':
        expression = member_1 - member_2
    else:
        expression = member_1 * member_2

    question = str(member_1) + ' ' + operator + ' ' + str(member_2)
    correct_answer = str(expression)

    return (question, correct_answer)
