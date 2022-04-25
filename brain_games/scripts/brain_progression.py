#! /usr/bin/env python

from brain_games.games_engine import play_game
from brain_games.games import progression_game


def main():
    play_game(progression_game)


if __name__ == '__main__':
    main()
