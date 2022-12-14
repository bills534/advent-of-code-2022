

def containmentCheck(input_a, input_b):
    a_min = int(input_a.split('-')[0])
    a_max = int(input_a.split('-')[1])
    b_min = int(input_b.split('-')[0])
    b_max = int(input_b.split('-')[1])

    if (a_min <= b_min) and (a_max >= b_max):
        print(f'1 - b inside of a: {input_a}; {input_b}')
        return 1
    elif (b_min <= a_min) and (b_max >= a_max):
        print(f'1 - a inside of b: {input_a}; {input_b}')
        return 1
    else:
        print(f'0 - uncontainment: {input_a}; {input_b}')
        return 0


fullContainCount = 0
rowcount = 1
with open(r"C:\Development\python\advent-of-code-2022\Day4\puzzle_input.txt") as cleaningPairs:
    for assignment in cleaningPairs:
        elf_a = assignment.split(',')[0]
        elf_b = assignment.split(',')[1]

        fullContainCount += containmentCheck(elf_a, elf_b)
        print(rowcount)
        rowcount += 1

print(fullContainCount)