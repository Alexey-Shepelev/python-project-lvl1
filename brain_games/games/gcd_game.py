#! /usr/bin/env python

from random import randint


game_rule = 'Find the greatest common divisor of given numbers.'


def get_question_and_solution():
    start_num = 1
    end_num = 10
    number_1 = randint(start_num, end_num)
    number_2 = randint(start_num, end_num)

    question = str(number_1) + ' ' + str(number_2)

    if number_1 < number_2:
        number_1, number_2 = number_2, number_1

    div_remainder = number_1 % number_2
    while div_remainder != 0:
        number_1 = number_2
        number_2 = div_remainder
        div_remainder = number_1 % number_2

    correct_answer = str(number_2)
    return(question, correct_answer)