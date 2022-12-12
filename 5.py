import os
import string
import re

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

getFile(5)

with open('5.txt') as input:
    # Part 1
    # It seemed faster to just do this instead of trying to parse it directly
    stacks = {
        1 : ['G','T','R','W'],
        2 : ['G','C','H','P','M','S','V','W'],
        3 : ['C','L','T','S','G','M'],
        4 : ['J','H','D','M','W','R','F'],
        5 : ['P','Q','L','H','S','W','F','J'],
        6 : ['P','J','D','N','F','M','S'],
        7 : ['Z','B','D','F','G','C','S','J'],
        8 : ['R','T','B'],
        9 : ['H','N','W','L','C']
    }

    # Start at line 10
    for move in input.readlines()[10:]:
        move = move.replace('move ', '')
        move = move.replace(' from ', ',')
        move = move.replace(' to ', ',')
        quant, start, end = move.split(',')
        
        for moves in range(0, int(quant)):
            stacks[int(end)].append(stacks[int(start)].pop())

    partOne = ''
    for i in stacks:
        partOne = partOne + stacks[i][-1]

    print(partOne)

    # Part 2
    input.seek(0)

    # It seemed faster to just do this instead of trying to parse it directly
    stacks = {
        1 : ['G','T','R','W'],
        2 : ['G','C','H','P','M','S','V','W'],
        3 : ['C','L','T','S','G','M'],
        4 : ['J','H','D','M','W','R','F'],
        5 : ['P','Q','L','H','S','W','F','J'],
        6 : ['P','J','D','N','F','M','S'],
        7 : ['Z','B','D','F','G','C','S','J'],
        8 : ['R','T','B'],
        9 : ['H','N','W','L','C']
    }

    # Start at line 10
    for move in input.readlines()[10:]:
        move = move.replace('move ', '')
        move = move.replace(' from ', ',')
        move = move.replace(' to ', ',')
        quant, start, end = move.split(',')
        
        stacks[int(end)].extend(stacks[int(start)][-int(quant):])
        del stacks[int(start)][-int(quant):]

    partTwo = ''
    for i in stacks:
        partTwo = partTwo + stacks[i][-1]

    print(partTwo)