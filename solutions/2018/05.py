"""
Puzzles 5a and 5b for 2018

See https://adventofcode.com/2018/day/5
"""
import os
import string

from common import util

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')


def _reactive(a, b):
    """Determine if two units (letters) will react."""
    return bool(abs(ord(a) - ord(b)) == 32)


def _reduce(material):
    """reduce a material to its stable form by causing reactions."""
    reduced, done = list(material), False

    while not done:
        reduced = [c for c in reduced if c]
        i, i_max, done = 0, len(reduced) - 1, True

        while i < i_max:
            if _reactive(reduced[i], reduced[i+1]):
                reduced[i], reduced[i+1] = None, None
                done = False
                i += 1
            i += 1

    return ''.join(reduced)


def _strip_unit_type(a, material):
    """Remove both polarities of a unit type (e.g., bB) from a material."""
    unit_type = (a.lower(), a.upper())
    return ''.join([c for c in material if c not in unit_type])


def run():
    answer, done = {'a': {}, 'b': {}}, False
    start_time = util.now()

    with open(os.path.join(INPUT_DIR, 'input05.dat'), 'r') as f:
        initial_material = f.read().strip()

    # part A

    reduced_material = _reduce(initial_material)
    answer['a'].update({'length': len(reduced_material), 'material': ''.join(reduced_material)})
    print('Part One answer is: %d' % answer['a']['length'])

    # part B

    attempts = []
    for letter in string.ascii_lowercase:
        print('reducing less %s' % letter)
        stripped_and_reduced = _reduce(_strip_unit_type(letter, initial_material))
        attempts.append({'unit_type': letter, 'size': len(stripped_and_reduced)})

    ranked = sorted(attempts, key=lambda d: d['size'])
    answer['b'].update(ranked[0])

    print('Part Two answer is: %d' % answer['b']['size'])

    # summary

    print('whole answer dict is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
