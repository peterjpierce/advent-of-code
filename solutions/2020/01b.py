"""
Puzzle 1b for 2020

See https://adventofcode.com/2020/day/1
"""
from common import util
import os

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')


def run():
    start_time, answer = util.now(), None

    with open(os.path.join(INPUT_DIR, 'input01.txt'), 'r') as f:
        values = sorted([int(v) for v in f.readlines()])

    def _get_answer(values):
        values_length = len(values)

        for i in range(0, values_length):
            for j in range(i + 1, values_length):
                for k in range(i + 2, values_length):
                    x, y, z = values[i], values[j], values[k]
                    if x + y + z == 2020:
                        return (x, y, z, x * y * z)

        return None

    print('answer is: %s' % str(_get_answer(values)))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
