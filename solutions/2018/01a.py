"""
Puzzle 1a for 2018

See https://adventofcode.com/2018/day/1
"""
from common import util
import os

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')


def run():
    starting_frequency, start_time, answer = 0, util.now(), 0
    
    with open(os.path.join(INPUT_DIR, 'input01.dat'), 'r') as f:
        answer = starting_frequency + sum([int(v) for v in f.readlines()])

    print('answer is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
