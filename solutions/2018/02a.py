"""
Puzzle 2a for 2018

See https://adventofcode.com/2018/day/2
"""
from common import util
import os

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')


def run():
    has_exactly = {2: 0, 3: 0}
    start_time = util.now()
    
    with open(os.path.join(INPUT_DIR, 'input02.dat'), 'r') as f:
        for line in f.readlines():
            entry = line.strip()
            histogram = {c: 0 for c in entry}
            
            for letter in entry:
                histogram[letter] += 1
                
            for looking_for in (2, 3):
                has_exactly[looking_for] += 1 if bool([k for k, v in histogram.items() if v == looking_for]) else 0
                
    answer = has_exactly[2] * has_exactly[3]

    print('answer is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
