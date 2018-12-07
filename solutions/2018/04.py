"""
Puzzles 4a and 4b for 2018

See https://adventofcode.com/2018/day/4
"""
from collections import OrderedDict
import os
import re

from common import util

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
REGEX = {
    'event': re.compile('^\s*\[(.*?)\]\s*(\S.*)\s*$'),
    'guard': re.compile('guard #(\d+)\s.*', re.I),
    'sleep': re.compile('^falls\s+asleep', re.I),
    'wake': re.compile('^wakes\s+up', re.I),
}


def run():
    unsorted_lines, answer = {}, {'a': {}, 'b': {}}
    start_time = util.now()
    
    with open(os.path.join(INPUT_DIR, 'input04.dat'), 'r') as f:
        for line in f.readlines():
            entry_time, entry = REGEX['event'].search(line).groups()
            unsorted_lines[entry_time] = entry
            
    observations, guard, nap_start, total_sleepage = OrderedDict(), None, 0, {}
    
    for key in sorted(unsorted_lines.keys()):
        entry = unsorted_lines[key]
        day, hour, minute = re.split('[\s:]', key)

        is_new_series = REGEX['guard'].search(entry)
        if is_new_series:
            guard = is_new_series.group(1)

        elif REGEX['sleep'].search(entry):
            nap_start = int(minute)

        elif REGEX['wake'].search(entry):
            if day not in observations:
                observations[day] = {'guard': guard, 'is_asleep': [False for i in range(60)]}
            for i in range(nap_start, int(minute)):
                observations[day]['is_asleep'][i] = True

    # part A

    for entry in observations.values():
        id = entry['guard']
        total_sleepage[id] = total_sleepage.get(id, 0) + len([y for y in entry['is_asleep'] if y])

    for k, v in total_sleepage.items():
        if v > answer['a'].get('sleepage', 0):
            answer['a'] = {'guard': k, 'sleepage': v}
        
    histograms = {}

    for observed in observations.values():
        id = observed['guard']
        if id not in histograms:
            histograms[id] = [0 for i in range(60)]
        for minute in [i for i, v in enumerate(observed['is_asleep']) if v]:
            histograms[id][minute] += 1

    for i, v in enumerate(histograms[answer['a']['guard']]):
        if v > answer['a'].get('max_per_minute', 0):
            answer['a'].update({'worst_minute': i, 'max_per_minute': v})

    print('Part One answer is: %d' % (int(answer['a']['guard']) * answer['a']['worst_minute']))
    
    # part B
    
    def _most_minute(guard_id, all_histograms):
        """Find the minute a guard naps most, and how many times."""
        ranked = sorted(
            [{'minute': i, 'count': v} for i, v in enumerate(all_histograms[guard_id])],
            key=lambda d: d['count']
        )
        return ranked[-1]
    
    ranked_likelies = sorted(
        [{'guard': k, 'most': _most_minute(k, histograms)} for k in histograms.keys()],
        key=lambda e: e['most']['count']
    )
    answer['b'].update(ranked_likelies[-1])
    
    print('Part Two answer is: %d' % (int(answer['b']['guard']) * answer['b']['most']['minute']))
    
    print('whole answer dict is: %s' % str(answer))
    print('  elapsed: %f seconds' % util.elapsed_since(start_time))


if __name__ == '__main__':
    run()
