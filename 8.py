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

def checkEdgeVisible(grid, posY, posX):
    # Check for left edge
    # print(f'Left visible poxX: {posX}')
    if posX == 0:
        return True
    # Check for right edge
    if posX == len(grid[posY]) - 1:
        return True
    # Check for top
    if posY == 0:
        return True
    # Check for bottom
    if posY == len(grid) - 1:
        return True

def leftVisible(grid, posY, posX):
    # Check for short trees
    if len([v for k, v in grid[posY].items() if int(k) < int(posX) and v >= grid[posY][posX]]) > 0:
        return False
    else:
        return True

def rightVisible(grid, posY, posX):
    # Check for short trees
    if len([v for k, v in grid[posY].items() if int(k) > int(posX) and v >= grid[posY][posX]]) > 0:
        return False
    else:
        return True

def upVisible(grid, posY, posX):
    # Check for short trees
    for row in range(0, posY):
        if grid[posY][posX] <= grid[row][posX]:
            return False
    return True

def downVisible(grid, posY, posX):
    # Check for short trees
    for row in range(posY + 1, len(grid)):
        if grid[posY][posX] <= grid[row][posX]:
            return False
    return True

def leftCount(grid, posY, posX):
    left_scenic_score = 0
    for i in range(posX - 1, -1, -1):
        if posX == 0:
            return left_scenic_score
        left_scenic_score += 1
        if grid[posY][i] >= grid[posY][posX]:
            return left_scenic_score
    return left_scenic_score
        

def rightCount(grid, posY, posX):
    right_scenic_score = 0
    for i in range(posX + 1, len(grid[posY])):
        if posX == len(grid[posY]) - 1:
            return right_scenic_score
        right_scenic_score += 1
        if grid[posY][i] >= grid[posY][posX]:
            return right_scenic_score
    return right_scenic_score

def upCount(grid, posY, posX):
    up_scenic_score = 0
    for i in range(posY - 1, -1, -1):
        if posY == 0:
            return up_scenic_score
        up_scenic_score += 1
        if grid[posY][posX] <= grid[i][posX]:
            return up_scenic_score
    return up_scenic_score

def downCount(grid, posY, posX):
    # Check for short trees
    down_scenic_score = 0
    for i in range(posY + 1, len(grid)):
        if posY == len(grid) - 1:
            return down_scenic_score
        down_scenic_score += 1
        if grid[posY][posX] <= grid[i][posX]:
            return down_scenic_score
    return down_scenic_score
 
day = datetime.datetime.now().day
getFile(day)

with open(f'{day}.txt') as input:
# with open('8-test.txt') as input:

    # Build Grid
    grid = {}
    rowCount = 0
    columnCount = 0
    for row in input.readlines():
        grid.setdefault(rowCount, {})
        for column in row.strip():
            grid[rowCount][columnCount] = int(column)
            columnCount += 1
        columnCount = 0
        rowCount += 1

    # Analyze Grid
    visible_count = 0
    scenic_scores = []
    for row in grid:
        for column in grid[row]:
            # Part 1
            if ( checkEdgeVisible(grid, int(row), int(column)) or
                leftVisible(grid, int(row), int(column)) or
                rightVisible(grid, int(row), int(column)) or
                upVisible(grid, int(row), int(column)) or
                downVisible(grid, int(row), int(column)) ):

                visible_count += 1

            # Part 2
            if ( leftCount(grid, int(row), int(column)) == None or
                   rightCount(grid, int(row), int(column)) == None or
                   upCount(grid, int(row), int(column)) == None or
                   downCount(grid, int(row), int(column)) == None):
                   total_scenic_score = 0
            else:
                total_scenic_score = ( leftCount(grid, int(row), int(column)) *
                                     rightCount(grid, int(row), int(column)) *
                                     upCount(grid, int(row), int(column)) *
                                     downCount(grid, int(row), int(column)) )
            scenic_scores.append(total_scenic_score)

    print(f'Part One: {visible_count}')
    print(f'Part Two: {max(scenic_scores)}')
