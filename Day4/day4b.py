

def containmentCheck(input_a, input_b):
    a_min = int(input_a.split('-')[0])
    a_max = int(input_a.split('-')[1])
    b_min = int(input_b.strip().split('-')[0])
    b_max = int(input_b.strip().split('-')[1])

    if b_min in range(a_min, a_max + 1) or b_max in range(a_min, a_max + 1):
        return 1
    elif a_min in range(b_min, b_max + 1) or a_max in range(b_min, b_max + 1):
        return 1
    else:
        return 0


fullContainCount = 0
rowcount = 1
with open(r"C:\Development\python\advent-of-code-2022\Day4\puzzle_input.txt") as cleaningPairs:
    for assignment in cleaningPairs:
        elf_a = assignment.split(',')[0]
        elf_b = assignment.split(',')[1]

        fullContainCount += containmentCheck(elf_a, elf_b)
        print(f'{rowcount}: {elf_a}; {elf_b.strip()} - {containmentCheck(elf_a, elf_b)}')
        rowcount += 1

print(fullContainCount)