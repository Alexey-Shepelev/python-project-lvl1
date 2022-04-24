#! /usr/bin/env python

from brain_games.games_engine import main_engine
from brain_games.games import calc_game


def main():
    main_engine(calc_game)


if __name__ == '__main__':
    main()
