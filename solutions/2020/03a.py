"""Puzzle 3a for 2020

See https://adventofcode.com/2020/day/3
"""
from common import util
import os

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
TREE_SYMBOL = '#'


def run():
    start_time, answer = util.now(), 0
    grid, x = None, 0

    with open(os.path.join(INPUT_DIR, 'input03.txt'), 'r') as f:
        grid = [l.strip() for l in f.readlines()]

    repeating_width = len(grid[0])

    def _is_tree(x, y):
        """Uses modulus math to extend the columns."""
        modulated_x = x % repeating_width
        return bool(grid[y][modulated_x] == TREE_SYMBOL)

    for y in range(len(grid)):
        if _is_tree(x, y):
            answer += 1
        x += 3

    print('answer is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
