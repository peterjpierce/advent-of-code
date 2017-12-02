"""
Puzzle 2b for 2017

See http://adventofcode.com/2017/day/2
"""
from os.path import abspath, dirname, join

from common import util


def evenly_divisible(row_data):
    """Get a list of tuples (x, y) where y evenly divides x."""
    pairs, ordered, size = [], sorted(row_data), len(row_data)
    for y in range(0, size - 1):
        for x in range(y + 1, size):
            if not ordered[x] % ordered[y]:
                pairs.append((ordered[x], ordered[y]))
    return pairs


def run():
    start_time, answer = util.now(), 0
    input_file = join(dirname(abspath(__file__)), 'inputs', 'input02.dat')

    with open(input_file, 'r') as f:
        for row in f:
            for x, y in evenly_divisible([int(d) for d in row.split()]):
                answer += int(x / y)

    print('answer is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
