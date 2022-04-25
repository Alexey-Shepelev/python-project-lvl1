#! /usr/bin/env python

from brain_games.games_engine import play_game
from brain_games.games import gcd_game


def main():
    play_game(gcd_game)


if __name__ == '__main__':
    main()
