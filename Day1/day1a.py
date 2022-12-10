
elfdict = {}
elfnumber = 1
runningtotal = 0

with open(r"C:\Development\python\advent-of-code-2022\Day1\puzzle_input.txt") as carrylist:
    for item in carrylist:
        if item != '\n':
            runningtotal += int(item)
        else:
            elfdict[elfnumber] = runningtotal
            elfnumber += 1
            runningtotal = 0

print(elfdict)
maxelf = max(elfdict, key=elfdict.get)
print(f'{maxelf}:{elfdict[maxelf]}')