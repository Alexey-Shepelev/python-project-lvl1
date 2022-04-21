#! /usr/bin/env python

from brain_games.games_engine import main_engine
from brain_games.games import gcd_game


def main():
    main_engine(gcd_game)


if __name__ == '__main__':
    main()