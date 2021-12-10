import numpy as np

def line_overlap_hor_vert(coords):

    max_coord = np.max(coords) + 1
    map = np.zeros(max_coord * max_coord)

    for line in coords:
        x1 = min(line[0], line[2])
        x2 = max(line[0], line[2])
        y1 = min(line[1], line[3])
        y2 = max(line[1], line[3])

        if x1 == x2:
            indices = [max_coord*x1+i for i in range(y1,y2+1)]
            np.add.at(map, indices, 1)
        elif y1 == y2:
            indices = [max_coord*i+y1 for i in range(x1,x2+1)]
            np.add.at(map, indices, 1)

    return len(np.where(map >= 2)[0])

def line_overlap_hor_vert_diag(coords):

    max_coord = np.max(coords) + 1
    map = np.zeros(max_coord * max_coord)

    for line in coords:
        x1, y1, x2, y2 = line
        if x1 == x2:
            y_min = min(y1, y2)
            y_max = max(y1, y2)
            indices = [max_coord*x1+i for i in range(y_min,y_max+1)]
            np.add.at(map, indices, 1)
        elif y1 == y2:
            x_min = min(x1, x2)
            x_max = max(x1, x2)
            indices = [max_coord*i+y1 for i in range(x_min,x_max+1)]
            np.add.at(map, indices, 1)
        elif abs(x1-x2) == abs(y1-y2):
            x_sign = np.sign(x2-x1)
            y_sign = np.sign(y2-y1)
            x_index = list(range(x1, x2+x_sign, x_sign))
            y_index = list(range(y1, y2+y_sign, y_sign))
            indices = [max_coord*x+y for x,y in zip(x_index, y_index)]
            np.add.at(map, indices, 1)

    return len(np.where(map >= 2)[0])

def parse_line(line):

    coord = line.split(' -> ')
    return [int(x) for n in coord for x in n.split(',') ]

if __name__ == '__main__':
    file = open('5-input.txt', 'r')
    lines = [line.strip() for line in file.readlines()]

    coords = list(map(parse_line, lines))
    print("Answer to first puzzle: ", line_overlap_hor_vert(coords))
    print("Answer to second puzzle: ", line_overlap_hor_vert_diag(coords))