"""
Puzzle 1a for 2020

See https://adventofcode.com/2020/day/1
"""
from common import util
import os

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')


def run():
    start_time, answer = util.now(), None

    with open(os.path.join(INPUT_DIR, 'input01.txt'), 'r') as f:
        values = sorted([int(v) for v in f.readlines()])

    for x in values:
        for y in reversed([n for n in values if n >= x]):
            if x + y == 2020:
                answer = (x, y, x * y)

        if answer:
            break

    print('answer is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
