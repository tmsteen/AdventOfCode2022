import os
import string
import re
import datetime

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

def adjacent(head_pos, tail_pos):
    # Determine if adjacent
    if (( abs(head_pos['col'] - tail_pos['col']) <= 1 and
        abs(head_pos['row'] - tail_pos['row']) <= 1) or
        (head_pos['col'] == tail_pos['col'] and
        head_pos['row'] == tail_pos['row'] )):
        touching = True
    else:
        touching = False
    
    # Determine where adjacent
    # Overlap
    if (head_pos['col'] == tail_pos['col'] and
        head_pos['row'] == tail_pos['row'] ):
        type = 'o'
    # Up
    if (head_pos['col'] == tail_pos['col'] and
        head_pos['row'] - tail_pos['row'] >= 1 ):
        type = 'u'
    # Down
    if (head_pos['col'] == tail_pos['col'] and
        head_pos['row'] - tail_pos['row'] < 0 ):
        type = 'd'
    # Left
    if (head_pos['col'] - tail_pos['col'] < 0 and
        head_pos['row'] == tail_pos['row'] ):
        type = 'l'
    # Right
    if (head_pos['col'] - tail_pos['col'] >= 1 and
        head_pos['row'] == tail_pos['row'] ):
        type = 'r'
    # UpRight
    if (head_pos['col'] - tail_pos['col'] >= 1 and
        head_pos['row'] - tail_pos['row'] >= 1 ):
        type = 'ur'
    # UpLeft
    if (head_pos['col'] - tail_pos['col'] < 0 and
        head_pos['row'] - tail_pos['row'] >= 1 ):
        type = 'ul'
    # DownRight
    if (head_pos['col'] - tail_pos['col'] >= 1 and
        head_pos['row'] - tail_pos['row'] < 0 ):
        type = 'dr'
    # DownLeft
    if (head_pos['col'] - tail_pos['col'] < 0 and
        head_pos['row'] - tail_pos['row'] < 0 ):
        type = 'dl'

    return touching, type

day = datetime.datetime.now().day
getFile(day)

# with open(f'{day}.txt') as input:
with open('9-test.txt') as input:
    visited_pos = set()
    tail_pos_count = 0
    head_pos = {'col': 0, 'row': 0}
    tail_pos = {'col': 0, 'row': 0}
    for move in input.readlines():
        dir, dist = move.split(' ')
        for i in range(0, int(dist)):
            if dir == 'R':
                head_pos['col'] += 1
            if dir == 'L':
                head_pos['col'] -= 1
            if dir == 'U':
                head_pos['row'] += 1
            if dir == 'D':
                head_pos['row'] -= 1
            touching, type = adjacent(head_pos, tail_pos)
            
            if touching:
                continue
            else:
                if type == 'r':
                    tail_pos['col'] += 1
                if type == 'l':
                    tail_pos['col'] -= 1
                if type == 'u':
                    tail_pos['row'] += 1
                if type == 'd':
                    tail_pos['row'] -= 1
                if type == 'ur':
                    tail_pos['col'] += 1
                    tail_pos['row'] += 1
                if type == 'ul':
                    tail_pos['col'] -= 1
                    tail_pos['row'] += 1
                if type == 'dr':
                    tail_pos['col'] += 1
                    tail_pos['row'] -= 1
                if type == 'dl':
                    tail_pos['col'] -= 1
                    tail_pos['row'] -= 1

                visited_pos.add(f"{tail_pos['col']}{tail_pos['row']}")


    print(f'Part One: {len(visited_pos) + 1}')
    # 6081
