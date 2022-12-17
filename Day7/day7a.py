from pathlib import Path

current_dir = Path('xxx')
filesystem_dict = {}
directorylist = []
with open(r"C:\Development\python\advent-of-code-2022\Day7\puzzle_input.txt") as moves:
    for line in moves:
        line = line.strip()
        line_split = line.split(' ')
        first_element = line_split[0]

        # handle directory changes
        if first_element == '$':
            if line_split[1] == 'ls':
                pass
            elif line_split[1] == 'cd':
                if line_split[2] == '..':
                    # using the path library, the current_dir is a 'path' object
                    # so were able to leverage that for going up a dir
                    current_dir = current_dir.parent
                    # print(f'cd; {current_dir}')

                else:
                    current_dir = current_dir.joinpath(line_split[2])
                    directorylist.append(str(current_dir))
                    # print(f'up; {current_dir}')
        
        elif first_element == 'dir':
            pass
        
        else:
            directoryAsString = str(current_dir).strip()
            # print(directoryAsString)
            # print(line)

            file_size = first_element
            file_name = line_split[1]
            if directoryAsString not in filesystem_dict:
                filesystem_dict[directoryAsString] = [[file_name, file_size]]
            else:
                filesystem_dict[directoryAsString].append([file_name, file_size])
        
        # print(current_dir)
        # print(filesystem_dict)


totalDirSizeDict = {}
for directory in directorylist:
    
    totalSize = 0

    for item in filesystem_dict:
        if directory in item:
            filelist = filesystem_dict[item]
            for file in filelist:
                # print(file)
                # xxx\bqm: [['vqv', '133711'], ['wwlv.vgv', '263237']]
                totalSize += int(file[1])
    
    totalDirSizeDict[directory] = totalSize

answernumber = 0
for thing in totalDirSizeDict:
    if totalDirSizeDict[thing] < 100000:
        print(thing, totalDirSizeDict[thing])
        answernumber += totalDirSizeDict[thing]


print(answernumber)