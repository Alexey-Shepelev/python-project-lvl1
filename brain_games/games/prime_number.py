#! /usr/bin/env python

from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_solution():
    question = randint(1, 1000)

    def is_prime(x):
        if x < 2:
            return('no')
        elif x == 2:
            return('yes')
        i = 2
        while i <= x ** (1 / 2):
            if x % i == 0:
                return('no')
            else:
                i += 1
        return('yes')

    correct_answer = is_prime(question)

    return (question, correct_answer)
