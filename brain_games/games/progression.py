from random import randint


GAME_RULE = 'What number is missing in the progression?'


def get_question_and_solution():
    start_number = randint(0, 900)
    range_length = randint(5, 10)
    range_step = randint(1, 5)
    random_index = randint(1, range_length - 1)

    progression = list(range(
        start_number, start_number + range_length * range_step, range_step))
    progression = [str(i) for i in progression]

    correct_answer = progression[random_index]

    progression[random_index] = '..'

    question = " ".join(progression)

    return (question, correct_answer)
