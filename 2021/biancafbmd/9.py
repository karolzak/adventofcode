from ctypes import pointer
import numpy as np



def explore_board(board, i, j, direction):

    poi = board[i,j]
    i_max, j_max = board.shape
    basin_pts = []
    i_indices = []
    j_indices = []

    if direction == 'left' and (j-1 >= 0):
        # if the diagonals are 9 then we cannot move further
        if board[i, j-1] == 9:
            if board[min(i+1, i_max-1), j] != 9:
                i_indices.append(min(i+1, i_max-1))
                j_indices.append(j-1)
            if board[max(i-1, 0), j] != 9:
                i_indices.append(max(i-1, 0))
                j_indices.append(j-1)
        else:
            for index in range(max(i-1, 0), min(i+2, i_max)):
                i_indices.append(index)
                j_indices.append(j-1)

    elif direction == 'right' and (j+1 < j_max):
        if board[i, j+1] == 9:
            if board[min(i+1, i_max-1), j] != 9:
                i_indices.append(min(i+1, i_max-1))
                j_indices.append(j+1)
            if board[max(i-1, 0), j] != 9:
                i_indices.append(max(i-1, 0))
                j_indices.append(j+1)
        else:
            for index in range(max(i-1, 0), min(i+2, i_max)):
                i_indices.append(index)
                j_indices.append(j+1)
    elif direction == 'up' and (i-1 >= 0):
        if board[i-1, j] == 9:
            if board[i, min(j+1, j_max-1)] != 9:
                i_indices.append(i-1)
                j_indices.append(min(j+1, j_max-1))
            if board[i, max(j-1, 0)] != 9:
                i_indices.append(i-1)
                j_indices.append(max(j-1, 0))
        else:
            for index in range(max(j-1, 0), min(j+2, j_max)):
                i_indices.append(i-1)
                j_indices.append(index)
    elif direction == 'down' and (i+1 < i_max):
        if board[i+1, j] == 9:
            if board[i, min(j+1, j_max-1)] != 9:
                i_indices.append(i+1)
                j_indices.append(min(j+1, j_max-1))
            if board[i, max(j-1, 0)] != 9:
                i_indices.append(i+1)
                j_indices.append(max(j-1, 0))
        else:
            for index in range(max(j-1, 0), min(j+2, j_max)):
                i_indices.append(i+1)
                j_indices.append(index)
    
    for i_index, j_index in zip(i_indices, j_indices):
        point = board[i_index, j_index]
        if point != 9 and (poi-point <= 0):
            if (i_index, j_index) not in basin_pts:
                basin_pts.append((i_index, j_index))
            boards = explore_board(board, i_index, j_index, direction)
            for b in boards:
                if b not in basin_pts:
                    basin_pts.append(b)

    return basin_pts

if __name__ == '__main__':
    file = open('9-input.txt', 'r')
    lines = [line.strip() for line in file.readlines()]
    
    board = np.array([[int(char) for char in line] for line in lines])

    x_right = board - np.roll(board,1)    
    x_right[:, 0] = -1
    x_left = board - np.roll(board,-1)
    x_left[:, -1] = -1
    x_down = board - np.roll(board,1, axis = 0)
    x_down[0, :] = -1 
    x_up = board - np.roll(board,-1, axis = 0)
    x_up[-1, :] = -1
 
    (x, y) = np.where(x_right&x_left&x_up&x_down<0)
    risk_level = sum([board[x[i]][y[i]]+1 for i in range(0, len(x))])

    print("Answer to first puzzle: ", risk_level)

    directions = ['left', 'right', 'up', 'down']
    sizes = []

    for i, j in zip(x, y):
        points = []
        points.append((i,j))
        for direction in directions:
            pts = explore_board(board, i, j, direction=direction)
            for point in pts:
                if point not in points:
                    points.append(point)

        sizes.append(len(points))

    sizes = sorted(sizes, reverse=True)
    print("Answer to second puzzle: ", np.prod(sizes[0:3]))