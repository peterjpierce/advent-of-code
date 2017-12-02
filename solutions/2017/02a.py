"""
Puzzle 2a for 2017

See http://adventofcode.com/2017/day/2
"""
from os.path import abspath, dirname, join

from common import util


def run():
    start_time, answer = util.now(), 0
    input_file = join(dirname(abspath(__file__)), 'inputs', 'input02.dat')

    def checksum(row_data):
        return max(row_data) - min(row_data) if any(row_data) else 0

    with open(input_file, 'r') as f:
        for row in f:
            answer += checksum([int(d) for d in row.split()])

    print('answer is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
