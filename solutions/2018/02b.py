"""
Puzzle 2b for 2018

See https://adventofcode.com/2018/day/1
"""
from common import util
import os

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')


def run():
    answer = None
    start_time = util.now()
    
    with open(os.path.join(INPUT_DIR, 'input02.dat'), 'r') as f:
        all_lines = [l.strip() for l in f.readlines()]
        
    for position in reversed(range(len(all_lines[0]))):
        have_seen = {}
        
        for word in all_lines:
            letters = list(word)
            del letters[position]
            minus_one = ''. join(letters)
            
            if minus_one in have_seen:
                answer = minus_one, word, have_seen[minus_one], position + 1
                break
                
            have_seen[minus_one] = word
            
        if answer:
            break
        
    print('answer is: %s (from %s and %s by masking position %d)' % answer)
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
