#! /usr/bin/env python

from brain_games.games import even_game
from brain_games.games_engine import main_engine


def main():
    main_engine(even_game)


if __name__ == '__main__':
    main()
