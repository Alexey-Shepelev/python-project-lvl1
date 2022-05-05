from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i <= x ** (1 / 2):
        if x % i == 0:
            return False
        i += 1
    return True


def get_question_and_solution():
    question = randint(1, 1000)
    correct_answer = 'yes' if is_prime(question) else 'no'

    return (question, correct_answer)
