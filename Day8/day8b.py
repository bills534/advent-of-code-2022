

# convert the input to a bunch of arrays
forestMap = []
with open(r"C:\Development\python\advent-of-code-2022\Day8\puzzle_input.txt") as map:
    for row in map:
        row = row.strip()
        currentRow = []
        for treeHeight in row:
            currentRow.append(int(treeHeight))

        forestMap.append(currentRow)


mapHeight = len(forestMap)
mapWidth = len(forestMap[0])

startingRow = 1
startingColumn = 1
lastRow = mapHeight - 2
lastColumn = mapWidth - 2
logOn = False


def isTreeVisible(rowX, columnY):
    startingTreeHeight = forestMap[rowX][columnY]
    north = False
    south = False
    west = False
    east = False
    countN = 0
    countS = 0
    countW = 0
    countE = 0
    if logOn:
        print(f'Current Tree: {startingTreeHeight}, ({columnY},{rowX})')
    
    # test north
    testRow = rowX
    while testRow - 1 >= 0:
        testRow -= 1
        testTree = forestMap[testRow][columnY]
        if logOn:
            print(f'-N; height:{testTree}, loc({columnY},{testRow})')
        if testTree >= startingTreeHeight:
            north = True
            countN += 1
            break
        else:
            countN += 1
        
    
    # test south
    testRow = rowX
    while testRow + 1 <= mapHeight - 1:
        testRow += 1
        testTree = forestMap[testRow][columnY]
        if logOn:
            print(f'-S; height:{testTree}, loc({columnY},{testRow})')
        if testTree >= startingTreeHeight:
            south = True
            countS += 1
            break
        else:
            countS += 1
        

    # test east
    testColumn = columnY
    while testColumn + 1 <= mapWidth - 1:
        testColumn += 1
        testTree = forestMap[rowX][testColumn]
        if logOn:
            print(f'-E; height:{testTree}, loc({testColumn},{rowX})')
        if testTree >= startingTreeHeight:
            east = True
            countE += 1
            break
        else:
            countE += 1


    # test west
    testColumn = columnY
    while testColumn - 1 >= 0:
        testColumn -= 1
        testTree = forestMap[rowX][testColumn]
        if logOn:
            print(f'-W; height:{testTree}, loc({testColumn},{rowX})')
        if testTree >= startingTreeHeight:
            west = True
            countW += 1
            break
        else:
            countW += 1


    visibleScore = (countN * countS * countW * countE)
    # print(f'{visibleScore}: {countN} * {countS} * {countW} * {countE}')
    # if hidden in all directions then tree is not visible
    if north and south and east and west:
        return False, visibleScore # tree is hidden
    else:
        if logOn:
            print(f'-Visible! - height:{startingTreeHeight}, loc({columnY},{rowX})')
        return True, visibleScore # tree is visible




currentColumn = startingColumn
currentRow = startingRow
visibleTrees = (mapHeight * 2) + (mapWidth -2) * 2
bestScore = 0
while currentColumn <= lastColumn:
    currentTree = forestMap[currentRow][currentColumn]
    #print(currentTree, isTreeVisible(currentRow, currentColumn))

    isVis, visibilityScore = isTreeVisible(currentRow, currentColumn)
    # print(visibilityScore)
    if isVis:
        visibleTrees += 1
    if visibilityScore > bestScore:
        bestScore = visibilityScore

    if currentColumn == lastColumn and currentRow != lastRow:
        currentRow += 1
        currentColumn = startingColumn
    elif currentColumn == lastColumn and currentRow == lastRow:
        break
    else:
        currentColumn += 1


print(f'visible trees: {visibleTrees}; Scenic Score: {bestScore}')