"""Puzzle 3b for 2020

See https://adventofcode.com/2020/day/3
"""
from common import util
import os

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
TREE_SYMBOL = '#'

SLOPES = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
)

def run():
    start_time, answer = util.now(), {}
    grid, x, slope_number = None, 0, 0

    with open(os.path.join(INPUT_DIR, 'input03.txt'), 'r') as f:
        grid = [l.strip() for l in f.readlines()]

    repeating_width = len(grid[0])

    def _is_tree(x, y):
        """Uses modulus math to extend the columns."""
        modulated_x = x % repeating_width
        return bool(grid[y][modulated_x] == TREE_SYMBOL)

    for move_x, move_y in SLOPES:
        x = 0
        slope_number += 1
        answer[slope_number] = 0

        for y in range(0, len(grid), move_y):
            if _is_tree(x, y):
                answer[slope_number] += 1
            x += move_x

        answer['product'] = answer.get('product', 1) * answer[slope_number]

    print('answer is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
