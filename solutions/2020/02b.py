"""Puzzle 2b for 2020

See https://adventofcode.com/2020/day/2
"""
from common import util
import re
import os

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
SPLITS_PATTERN = re.compile(r'-|\s+|:\s*')


def run():
    start_time, answer = util.now(), None

    with open(os.path.join(INPUT_DIR, 'input02.txt'), 'r') as f:
        lines = f.readlines()

    def _is_valid(entry):
        parts = [p for p in SPLITS_PATTERN.split(entry.strip())]
        index_a, index_b, required, given = int(parts[0]) - 1, int(parts[1]) - 1, parts[2], parts[3]
        matches = [i for i in (index_a, index_b) if given[i] == required]
        return bool(len(matches) == 1)

    valid_entries = [e for e in lines if _is_valid(e)]
    answer = len(valid_entries)

    print('answer is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
