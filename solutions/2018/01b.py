"""
Puzzle 1b for 2018

See https://adventofcode.com/2018/day/1
"""
from common import util
import os

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')


def repeating_iterator(finite_list):
    """An iterator that repeats a finite list forever."""
    idx, values_count = 0, len(finite_list)

    while True:
        yield finite_list[(idx % values_count)]
        idx += 1


def run():
    current_frequency, answer, tried, already_seen = 0, 0, 0, set()
    start_time = util.now()
    
    with open(os.path.join(INPUT_DIR, 'input01.dat'), 'r') as f:
        all_values = [int(v) for v in f.readlines()]
       
    for value in repeating_iterator(all_values):
        current_frequency += int(value)
        tried += 1

        if current_frequency in already_seen:
            answer = current_frequency
            break
        
        already_seen.add(current_frequency)

    print('answer is: %s (found after %d changes)' % (str(answer), tried))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
