"""
Puzzle 1a for 2019

See https://adventofcode.com/2019/day/1
"""
from common import util
import os

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')


def run():
    start_time, answer = util.now(), 0

    with open(os.path.join(INPUT_DIR, 'input01.dat'), 'r') as f:
        answer = sum([int(int(v) / 3) - 2 for v in f.readlines()])

    print('answer is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
