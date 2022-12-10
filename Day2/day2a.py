


points = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

def calcscore(elf, me):
    elfvalue = points[elf]
    myvalue = points[me]
    rpsScore = myvalue

    rpsResult = myvalue - elfvalue

    # since losses result in 0 points, only calculate scores for draws and wins
    # ex scissors vs paper
    if rpsResult == 1:
        rpsScore += 6
    # rock vs scissors
    elif rpsResult == -2:
        rpsScore += 6
    elif rpsResult == 0:
        rpsScore += 3
    
    return rpsScore

totalScore = 0
with open(r"C:\Development\python\advent-of-code-2022\Day2\puzzle_input.txt") as movelist:
    for move in movelist:
        elfmove = move.split(' ')[0]
        mymove = move.strip().split(' ')[1]

        totalScore += calcscore(elfmove, mymove)

print(totalScore)

