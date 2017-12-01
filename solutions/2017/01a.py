"""
Puzzle 1a for 2017

See http://adventofcode.com/2017/day/1
"""
from os.path import abspath, dirname, join

from common import util

INPUT = join(dirname(abspath(__file__)), 'inputs', 'input01a.dat')


def run():
    start_time = util.now()

    with open(INPUT, 'r') as f:
        digits = f.read().strip()

    wrapped = digits + digits[0]
    answer = sum([int(d) for i, d in enumerate(digits) if d == wrapped[i+1]])

    print('answer is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
