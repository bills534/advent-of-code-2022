from pprint import pprint

stacks = {
    1: ['D', 'B', 'J', 'V'],
    2: ['P', 'V', 'B', 'W', 'R', 'D', 'F'],
    3: ['R', 'G', 'F', 'L', 'D', 'C', 'W', 'Q'],
    4: ['W', 'J', 'P', 'M', 'L', 'N', 'D', 'B'],
    5: ['H', 'N', 'B', 'P', 'C', 'S', 'Q'],
    6: ['R', 'D', 'B', 'S', 'N', 'G'],
    7: ['Z', 'B', 'P', 'M', 'Q', 'F', 'S', 'H'],
    8: ['W', 'L', 'F'],
    9: ['S', 'V', 'F', 'M', 'R']
}

# move 1 from 4 to 1
# move 2 from 4 to 8
# move 5 from 9 to 6


with open(r"C:\Development\python\advent-of-code-2022\Day5\puzzle_input.txt") as moves:
    for move in moves:
        move = move.strip()
        numberOfContainers = int(move.split(' ')[1])
        fromStack = int(move.split(' ')[3])
        toStack = int(move.split(' ')[5])

        containersInMotion = stacks[fromStack][-numberOfContainers:]
        containersStayingBehind = stacks[fromStack][:-numberOfContainers]
        stacks[fromStack] = containersStayingBehind
        stacks[toStack] = stacks[toStack] + containersInMotion
        


for stack in stacks:
    print(stacks[stack])