"""
Puzzle 1a for 2019

See https://adventofcode.com/2019/day/1
"""
from common import util
import os

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')


def fuel_needed(given_weight):
    return max(int(given_weight / 3) - 2, 0)


def run():
    start_time, answer = util.now(), 0

    with open(os.path.join(INPUT_DIR, 'input01.dat'), 'r') as f:
        for row in f.readlines():
            fuel = fuel_needed(int(row))

            while fuel > 0:
                answer += fuel
                fuel = fuel_needed(fuel)

    print('answer is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
