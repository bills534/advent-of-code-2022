


def getLetterValue(inputLetter):
    startingValue = ord(inputLetter)
    outputValue = 0
    # ord('a') = 97, ord('A') = 65; so we convert them to the ranges we need
    if startingValue >= 97:
        outputValue = (startingValue - 96)
    else:
        outputValue = (startingValue - 38)
    
    return outputValue


totalPriority = 0

allContents = []
with open(r"C:\Development\python\advent-of-code-2022\Day3\puzzle_input.txt") as rucksackContents:
    for content in rucksackContents:
        content = content.strip()
        allContents.append(content)

sack = 0
badgeLetter = ''
while sack < len(allContents):
    firstbag = allContents[sack]
    secondbag = allContents[sack + 1]
    thirdbag = allContents[sack + 2]

    for item in firstbag:
        if item in secondbag and item in thirdbag:
            badgeLetter = item

    totalPriority += getLetterValue(badgeLetter)
    sack += 3


print(totalPriority)
