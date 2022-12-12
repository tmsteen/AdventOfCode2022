import os
import string
import re
import datetime
from math import floor, prod

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

with open(f'11.txt') as input:
# with open('11-test.txt') as input:
    monkeys = {}
    iterator = iter(input.readlines())
    for monkey in iterator:
        monkeys[int(monkey.strip().split(' ')[-1].replace(':', ''))] = {
            'starting_items': next(iterator).strip().split(': ')[1].split(', '),
            'operation': next(iterator).strip().split(': ')[1].split(' = ')[-1],
            'test': int(next(iterator).strip().split(' ')[-1]),
            'true_case': int(next(iterator).strip().split(' ')[-1]),
            'false_case': int(next(iterator).strip().split(' ')[-1]),
            'inspected_count': 0
        }
        # Skip empty line
        try:
            next(iterator)
        except:
            break

    mod_factor = prod(monkeys[monkey]['test'] for monkey in monkeys)

    for round in range(0,10000):
        print(round)
        for monkey in monkeys:
            for item in tuple(monkeys[monkey]['starting_items']): 
                monkeys[monkey]['inspected_count'] += 1
                # Calculate worry level
                old = int(item)
                new = eval(monkeys[monkey]['operation'])
                
                # Monkey gets board, foor divide by 3 -- part 1 only
                # new = floor(new / 3)

                # Manage worry level
                new %= mod_factor

                # Test condition
                if new % int(monkeys[monkey]['test']) == 0:
                    monkeys[monkeys[monkey]['true_case']]['starting_items'].append(new)
                else:
                    monkeys[monkeys[monkey]['false_case']]['starting_items'].append(new)
                
                # Remove item that was thrown
                del(monkeys[monkey]['starting_items'][0])

    totals = []
    for monkey in monkeys:
        totals.append(monkeys[monkey]['inspected_count'])
    sorted_totals = sorted(totals)
    print(sorted_totals[-1] * sorted_totals[-2])
