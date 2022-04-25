#! /usr/bin/env python

from random import randint


GAME_RULE = 'What number is missing in the progression?'


def get_question_and_solution():

    start_num = 0
    end_num = 90

    start_number = randint(start_num, end_num)
    range_length = randint(5, 10)
    range_step = randint(1, 5)
    random_index = randint(1, range_length - 1)

    numbers_list = list(range(
        start_number, start_number + range_length * range_step, range_step))
    numbers_list = [str(i) for i in numbers_list]

    correct_answer = numbers_list[random_index]

    numbers_list[random_index] = '..'

    question = " ".join(numbers_list)

    return (question, correct_answer)
