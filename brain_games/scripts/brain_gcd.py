#! /usr/bin/env python

from brain_games.games_engine import play
from brain_games.games import gcd


def main():
    play(gcd)


if __name__ == '__main__':
    main()
