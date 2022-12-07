def elf_with_most_calories():
    # initialise lists
    items = []
    elves = [[]]
    calories = []

    # read input file
    with open('input.txt', 'r') as input:
        for line in input:
            items.append(line.strip())

    # assign items to elves
    delimiter = ''
    for item in items:
        if item == delimiter:
            elves.append([])
        elif item != delimiter:
            elves[-1].append(int(item))

    # calculate calories carried per elf
    for elf in elves:
        calories.append(sum(elf))

    # print the max calories carried by an elf
    return calories


def top_three_calories(calories):
    total = 0
    # remove the largest calorie and add it to total
    for _ in range(3):
        largest = max(calories)
        total += largest
        calories.remove(largest)
    print(total)
    return
