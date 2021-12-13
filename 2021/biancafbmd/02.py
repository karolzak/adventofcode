def get_position(course):

    horz = 0
    depth = 0

    for instr in course:
        
        x = int(instr.strip()[-1])
        if 'forward' in instr:
            horz += x
        elif 'down' in instr:
            depth += x
        elif 'up' in instr:
            depth -= x
        else:
            print("course does not contain accepted instructions")

    return horz, depth

def get_position_with_aim(course):

    horz = 0
    depth = 0
    aim = 0

    for instr in course:
        
        x = int(instr.strip()[-1])
        if 'forward' in instr:
            horz += x
            depth += aim * x
        elif 'down' in instr:
            aim += x
        elif 'up' in instr:
            aim -= x
        else:
            print("course does not contain accepted instructions")

    return horz, depth

if __name__ == '__main__':
    file1 = open('2-input.txt', 'r')
    lines = file1.readlines()

    horz, depth = get_position(lines)
    print("horizontal position: ", horz, "depth: ", depth)
    print("Answer to first puzzle: ", horz*depth)

    horz, depth = get_position_with_aim(lines)
    print("horizontal position: ", horz, "depth: ", depth)
    print("Answer to second puzzle: ", horz*depth)