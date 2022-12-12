# A - Rock
# B - Paper
# C - Scissors
# X - Rock
# Y - Paper
# Z - Scissors

scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'lost': 0,
    'draw': 3,
    'win': 6
}

total_score_1 = 0
total_score_2 = 0

with open('2.txt') as input:
    for round in input.readlines():
        elf,move = round.strip().split(' ')

        # Part 1 Logic
        # Case Elf Wins
        if ((elf == 'A' and move == 'Z') or
            (elf == 'B' and move == 'X') or
            (elf == 'C' and move == 'Y')):
            result1 = 'lost'
        # Case I Win
        elif ((elf == 'A' and move == 'Y') or
              (elf == 'B' and move == 'Z') or
              (elf == 'C' and move == 'X')):
            result1 = 'win'
        # Case Draw
        elif ((elf == 'A' and move == 'X') or
              (elf == 'B' and move == 'Y') or
              (elf == 'C' and move == 'Z')):
            result1 = 'draw'

        total_score_1 += scores[move] + scores[result1]

        # Part 2 Logic
        # A - Rock
        # B - Paper
        # C - Scissors
        # X - Lose
        # Y - Draw
        # Z - Win
        # Case I Chose Rock
        if ((elf == 'A' and move == 'Y') or
            (elf == 'B' and move == 'X') or
            (elf == 'C' and move == 'Z')):
            result2 = 'X'
        # Case I Chose Paper
        elif ((elf == 'A' and move == 'Z') or
              (elf == 'B' and move == 'Y') or
              (elf == 'C' and move == 'X')):
            result2 = 'Y'
        # Case I Chose Scissors
        elif ((elf == 'A' and move == 'X') or
              (elf == 'B' and move == 'Z') or
              (elf == 'C' and move == 'Y')):
            result2 = 'Z'

        if move == 'X':
            move_word = 'lost'
        elif move == 'Y':
            move_word = 'draw'
        elif move == 'Z':
            move_word = 'win'

        total_score_2 += scores[move_word] + scores[result2]

    print(f'Part 1: {total_score_1}')
    print(f'Part 2: {total_score_2}')
