"""
Puzzle 3a for 2017

See http://adventofcode.com/2017/day/3
"""
from common import util


class Grid:
    """Navigate grid values."""
    clockwise = ('left', 'up', 'right', 'down')

    def __init__(self):
        self.ring = None
        self.x = None
        self.y = None

    def find_position(self, puzzle_input):
        self.ring = self._which_ring(puzzle_input)
        self.x = self.ring
        self.y = self.ring * -1

        current_value = self._ring_max(self.ring)

        if current_value == puzzle_input:
            return self.x, self.y

        for direction in self.clockwise:
            unwind = getattr(self, direction)

            while current_value:
                unwind(1)
                current_value -= 1

                if current_value == puzzle_input:
                    return self.x, self.y
                elif self.at_corner:
                    break

    @property
    def at_corner(self):
        return bool(abs(self.x) == self.ring and abs(self.y) == self.ring)

    def up(self, distance):
        self.y += distance

    def down(self, distance):
        self.y -= distance

    def right(self, distance):
        self.x += distance

    def left(self, distance):
        self.x -= distance

    @staticmethod
    def _ring_max(ring_number):
        return pow((2 * ring_number) + 1, 2)

    def _which_ring(self, value):
        index = 0

        while True:
            if self._ring_max(index) >= value:
                return index
            index += 1


def run():
    start_time, answer = util.now(), 0
    puzzle_input = 289326

    grid = Grid()
    x, y = grid.find_position(puzzle_input)
    answer = abs(x) + abs(y)

    print('answer is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
