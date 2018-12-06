"""
Puzzle 3a for 2018

See https://adventofcode.com/2018/day/3
"""
from collections import namedtuple
from common import util
import os
import re

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
INPUT_REGEX = re.compile('^\s*\#(\d+)\s*\@\s*(\d+),(\d+):\s*(\d+)\s*x\s*(\d+)\s*$')
SquareSpecification = namedtuple('SquareDefinition', 'id x y width height')


def _define_square(input_row):
    """data looks like: #1269 @ 401,564: 22x29 """
    hit = INPUT_REGEX.search(input_row)
    if hit:
        return SquareSpecification._make([int(g) for g in hit.groups()])
    print('input "%s" is malformed' % input_row)


def run():
    grid, answer = [], 0
    start_time = util.now()
    
    with open(os.path.join(INPUT_DIR, 'input03.dat'), 'r') as f:
        all_squares = [_define_square(l) for l in f.readlines() if l.strip()]
        
    max_x = max([s.x + s.width for s in all_squares])
    max_y = max([s.y + s.height for s in all_squares])

    for i in range(max_y + 1):
        grid.append([[] for j in range(max_x + 1)])
    
    for square in all_squares:
        for i in range(square.y, square.y + square.height):
            for j in range(square.x, square.x + square.width):
                grid[i][j].append(square.id)
    
    for row in grid:
        for column in row:
            if len(column) > 1:
                answer += 1
        
    print('answer is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
