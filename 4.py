import os
import string

import requests


def getFile(day):
    path = f'./{day}.txt'
    if not os.path.isfile(path):
        headers = {
            'cookie': 'session='
        }
        r = requests.get(f'https://adventofcode.com/2022/day/{day}/input', headers=headers)
        f = open(f'./{day}.txt', 'x')
        f.write(r.text)
        f.close()

def split(input):
    ruckSize = int(len(input.strip()) / 2)
    return input[:ruckSize].strip(), input[ruckSize:].strip()

def getPriority(input):
    return string.ascii_letters.index(input) + 1

getFile(4)
completeOverlaps = 0
partialOverlaps = 0

with open('4.txt') as input:
    for assignment in input.readlines():
        rangePairOne, rangePairTwo = assignment.split(',')
        rangeOneStart, rangeOneEnd = rangePairOne.split('-')
        rangeTwoStart, rangeTwoEnd = rangePairTwo.split('-')
        rangeOne = range(int(rangeOneStart), int(rangeOneEnd) + 1)
        rangeTwo = range(int(rangeTwoStart), int(rangeTwoEnd) + 1)

        # Part 1
        if ( rangeOne[0] in rangeTwo and rangeOne[-1] in rangeTwo or
            rangeTwo[0] in rangeOne and rangeTwo[-1] in rangeOne ):
            completeOverlaps += 1

        # Part 2
        if any(x in rangeOne for x in rangeTwo):
            partialOverlaps += 1

    print(f'Complete Overlaps: {completeOverlaps}')
    print(f'Partial Overlaps: {partialOverlaps}')




