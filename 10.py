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

day = datetime.datetime.now().day
getFile(day)

with open(f'{day}.txt') as input:
# with open('10-test.txt') as input:
    cycle = 0
    reg_x = 1
    history = {}
    crt = {}
    for i in range(1, 240):
        crt[i] = '.'
    for instruction in input.readlines():
        cycle += 1
        if instruction.strip() == 'noop':
            history[cycle] = reg_x
        else:
            command, value = instruction.strip().split(' ')
            history[cycle] = reg_x
            cycle += 1
            history[cycle] = reg_x
            reg_x += int(value)
 
    # Calculate signal strengths
    signal_sum = 0
    for i in history:
        if ( i % 40 == 20 ):
            signal_sum += i * history[i]

        if history[i] - 1 == (i-1) % 40:
            crt[i] = '#'
        elif history[i] == (i-1) % 40:
            crt[i] = '#'
        elif history[i] + 1 == (i-1) % 40:
            crt[i] = '#'

    print(f'Part One: {signal_sum}')
    for i in crt:
        print(crt[i], end=''),
        if i % 40 == 0:
            print('\n', end=''),
        
