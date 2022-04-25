#! /usr/bin/env python

from brain_games.games_engine import play_game
from brain_games.games import calculator


def main():
    play_game(calculator)


if __name__ == '__main__':
    main()
