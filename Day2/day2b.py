


points = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
    "X": 0,  # Lose
    "Y": 3,  # Draw
    "Z": 6,  # Win
}

def calcscore(elf, neededResult):
    elfvalue = points[elf]
    myvalue = points[neededResult]
    rpsScore = myvalue

    # this isnt pretty but it works
    if myvalue == 0:
        if elfvalue == 3:    # scissor
            rpsScore += 2    # rock
        elif elfvalue == 2:  # paper
            rpsScore += 1    # rock
        else:                # rock
            rpsScore += 3    # paper

    elif myvalue == 3:
        rpsScore += elfvalue

    elif myvalue == 6:
        if elfvalue == 3:
            rpsScore += 1
        else:
            rpsScore += (elfvalue + 1)

    # print(f'elf: {elfvalue}, me:{myvalue} = {rpsScore}')
    return rpsScore

totalScore = 0
with open(r"C:\Development\python\advent-of-code-2022\Day2\puzzle_input.txt") as movelist:
    for move in movelist:
        elfmove = move.split(' ')[0]
        mymove = move.strip().split(' ')[1]

        totalScore += calcscore(elfmove, mymove)

print(totalScore)

