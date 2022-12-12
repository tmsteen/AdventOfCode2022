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

def adjacent(pos1, pos2):
    # Determine if adjacent
    if (( abs(pos1['col'] - pos2['col']) <= 1 and
        abs(pos1['row'] - pos2['row']) <= 1) or
        (pos1['col'] == pos2['col'] and
        pos1['row'] == pos2['row'] )):
        touching = True
    else:
        touching = False
    
    # Determine where adjacent
    # Overlap
    if (pos1['col'] == pos2['col'] and
        pos1['row'] == pos2['row'] ):
        type = 'o'
    # Up
    if (pos1['col'] == pos2['col'] and
        pos1['row'] - pos2['row'] >= 1 ):
        type = 'u'
    # Down
    if (pos1['col'] == pos2['col'] and
        pos1['row'] - pos2['row'] < 0 ):
        type = 'd'
    # Left
    if (pos1['col'] - pos2['col'] < 0 and
        pos1['row'] == pos2['row'] ):
        type = 'l'
    # Right
    if (pos1['col'] - pos2['col'] >= 1 and
        pos1['row'] == pos2['row'] ):
        type = 'r'
    # UpRight
    if (pos1['col'] - pos2['col'] >= 1 and
        pos1['row'] - pos2['row'] >= 1 ):
        type = 'ur'
    # UpLeft
    if (pos1['col'] - pos2['col'] < 0 and
        pos1['row'] - pos2['row'] >= 1 ):
        type = 'ul'
    # DownRight
    if (pos1['col'] - pos2['col'] >= 1 and
        pos1['row'] - pos2['row'] < 0 ):
        type = 'dr'
    # DownLeft
    if (pos1['col'] - pos2['col'] < 0 and
        pos1['row'] - pos2['row'] < 0 ):
        type = 'dl'

    return touching, type

day = datetime.datetime.now().day
getFile(day)

with open(f'{day}.txt') as input:
# with open('9-test.txt') as input:
    visited_pos = set()
    tail_pos_count = 0
    positions = {0: {'col': 0, 'row': 0},
                 1: {'col': 0, 'row': 0},
                 2: {'col': 0, 'row': 0},
                 3: {'col': 0, 'row': 0},
                 4: {'col': 0, 'row': 0},
                 5: {'col': 0, 'row': 0},
                 6: {'col': 0, 'row': 0},
                 7: {'col': 0, 'row': 0},
                 8: {'col': 0, 'row': 0},
                 9: {'col': 0, 'row': 0},
     }
    for move in input.readlines():
        dir, dist = move.split(' ')
        for i in range(0, int(dist)):
            if dir == 'R':
                positions[0]['col'] += 1
            if dir == 'L':
                positions[0]['col'] -= 1
            if dir == 'U':
                positions[0]['row'] += 1
            if dir == 'D':
                positions[0]['row'] -= 1
            for pos in range(0, len(positions) - 1):
                touching, type = adjacent(positions[pos], positions[pos + 1])
                
                if touching:
                    continue
                else:
                    if type == 'r':
                        positions[pos + 1]['col'] += 1
                    if type == 'l':
                        positions[pos + 1]['col'] -= 1
                    if type == 'u':
                        positions[pos + 1]['row'] += 1
                    if type == 'd':
                        positions[pos + 1]['row'] -= 1
                    if type == 'ur':
                        positions[pos + 1]['col'] += 1
                        positions[pos + 1]['row'] += 1
                    if type == 'ul':
                        positions[pos + 1]['col'] -= 1
                        positions[pos + 1]['row'] += 1
                    if type == 'dr':
                        positions[pos + 1]['col'] += 1
                        positions[pos + 1]['row'] -= 1
                    if type == 'dl':
                        positions[pos + 1]['col'] -= 1
                        positions[pos + 1]['row'] -= 1

                    if pos + 1 == 9:
                        visited_pos.add(f"{positions[pos + 1]['col']}{positions[pos + 1]['row']}")


    print(f'Part Two: {len(visited_pos) + 1}')
    # 6081
