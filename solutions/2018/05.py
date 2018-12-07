"""
Puzzles 5a and 5b for 2018

See https://adventofcode.com/2018/day/5
"""
import os

from common import util

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')


def _reactive(a, b):
    """Determine if two polymers (letters) will react."""
    return bool(abs(ord(a) - ord(b)) == 32)


def run():
    answer, done = {'a': {}, 'b': {}}, False
    start_time = util.now()
    
    with open(os.path.join(INPUT_DIR, 'input05.dat'), 'r') as f:
        material = f.read().strip()
        
    while not done:
        material = [c for c in material if c]
        i, i_max = 0, len(material) - 1
        done = True
        
        while i < i_max:
            if _reactive(material[i], material[i+1]):
                material[i], material[i+1] = None, None
                done = False
                i += 1
            i += 1
        
    answer['a'].update({'length': len(material), 'material': ''.join(material)})

    print('Part One answer is: %d' % answer['a']['length'])
    
    # part B
    
    print('whole answer dict is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
