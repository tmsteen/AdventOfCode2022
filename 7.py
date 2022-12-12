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
# with open('test7.txt') as input:
    sizes = {}
    currentDirectory = ''

    # This sections gets me the total size of FILES in each directory
    # but does not take into account subdirectories
    for line in input.readlines():
        # Case when cd
        if line.startswith('$ cd'):
            directory = line.split(' ')[-1].strip()
            if directory == '..':
                currentDirectory = '/'.join(currentDirectory.split('/')[:-1])
                if currentDirectory == '':
                    currentDirectory = '/'
            elif directory == '/':
                currentDirectory = '/'
            else:
                if currentDirectory == '/':
                    currentDirectory = currentDirectory + directory
                else:
                    currentDirectory = currentDirectory + '/' + directory

            sizes.setdefault(currentDirectory, 0)
        elif line[0].isdigit():
            if currentDirectory not in sizes:
                sizes[currentDirectory] = int(line.split(' ')[0])
            else:
                sizes[currentDirectory] += int(line.split(' ')[0])

    print(sizes)
    # This section rolls up sub-directories so I have an accurate count of size
    # for the directory and all subs
    sizesRollup = {}
    for item in sizes:
        # print(item + ' '+ str(sizes[item]))
        sizesRollup[item] = sum(v for k,v in sizes.items() if k.startswith(item))

    partOne = sum([x for x in sizesRollup.values() if x <= 100000])
    print(f'Part One: {partOne}')
    # Correct answer is 1348005

    # Part 2
    totalUsed = sizesRollup['/']
    print(totalUsed)
    freeSpace = 70000000 - totalUsed
    neededSpace = 30000000 - freeSpace
    sortedRollup = dict(sorted(sizesRollup.items(), key=lambda item: item[1]))
    for dir in sortedRollup:
        if sortedRollup[dir] > neededSpace:
            print(f'Part Two: {sortedRollup[dir]}')
            break
