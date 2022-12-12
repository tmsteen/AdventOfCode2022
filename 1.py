calories = {}
elf = 0


with open('1.txt') as input:
    current_count = 0
    for item in input.readlines():
        if item.strip():
            current_count += int(item.strip())
        else:
            calories[elf] = current_count
            current_count = 0
            elf += 1

sorted_cals = dict(sorted(calories.items(), key=lambda item: item[1]))

# Answer to Part 1
print(list(sorted_cals.values())[-1])

# Anwer to Part 2
print(sum(list(sorted_cals.values())[-3:]))