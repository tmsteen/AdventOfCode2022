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

day = 3
errors = []
priorityTotal = 0

getFile(day)
with open(f'{day}.txt') as input:
    # Part 1
    print(f'Got {len(input.readlines())} Lines')
    input.seek(0)
    for line in input.readlines():
        ruckOne, ruckTwo = split(line)
        # print(f'{ruckOne}, {ruckTwo}')
        for item in ruckOne:
            if item in ruckTwo:
                errors.append(item)
                break

    print(f'Got {len(errors)} Errors')

    # print(errors)
    for error in errors:
        priorityTotal += getPriority(error)

    print(f'Part 1: {priorityTotal}')

    # Part 2
    input.seek(0)
    elves = input.readlines()
    index = 0
    badges = 0
    while True:
        try:
            elfOne = elves.pop(0)
            elfTwo = elves.pop(0)
            elfThree = elves.pop(0)
        except IndexError:
            break

        for item in elfOne:
            if item in elfTwo and item in elfThree:
                badges += getPriority(item)
                break

    print(f'Part 2: {badges}')
