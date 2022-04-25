#! /usr/bin/env python

from brain_games.games import even_game
from brain_games.games_engine import play_game


def main():
    play_game(even_game)


if __name__ == '__main__':
    main()
