#! /usr/bin/env python

from brain_games.games import even_number
from brain_games.games_engine import play_game


def main():
    play_game(even_number)


if __name__ == '__main__':
    main()
