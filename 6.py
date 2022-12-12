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

def split(input):
    ruckSize = int(len(input.strip()) / 2)
    return input[:ruckSize].strip(), input[ruckSize:].strip()

def getPriority(input):
    return string.ascii_letters.index(input) + 1

def unique(list1):
 
    # initialize a null list
    unique_list = []
 
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # Return uniqueness
    if len(list1) == len(unique_list):
        return True
    else:
        return False
 

getFile(datetime.datetime.now().day)

with open('6.txt') as input:
    datastream = input.readlines()[0]
    # Part 1
    for i in range(0, len(datastream)):
        if unique(datastream[i:i+4]):
            # Plus 4 because packet starts after current 4 char chunk
            print(f'Start of Packet: {i + 4}')
            break

    # Part 2
    for i in range(0, len(datastream)):
        if unique(datastream[i:i+14]):
            # Plus 4 because packet starts after current 4 char chunk
            print(f'Start of Message: {i + 14}')
            break
