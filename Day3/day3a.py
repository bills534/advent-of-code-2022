


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
with open(r"C:\Development\python\advent-of-code-2022\Day3\puzzle_input.txt") as rucksackContents:
    for content in rucksackContents:
        content = content.strip()
        halfItemCount = int(len(content) / 2)
        compartmentA = content[:halfItemCount]
        compartmentB = content[halfItemCount:]
        print(f'contents: {content}; itemcount: {halfItemCount}; A: {compartmentA}; B: {compartmentB}')

        commonItem = ''
        for item in compartmentA:
            if item in compartmentB:
                commonItem = item
                break
        
        totalPriority += getLetterValue(commonItem)

print(totalPriority)