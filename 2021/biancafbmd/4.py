import numpy as np

def get_winning_bingo_board(draw_list, boards):

    # create tracker array
    tracker = np.zeros((len(boards),2,5))
    board_sum = list(map(sum, boards))

    for number in draw_list:
        for b_index, board in enumerate(boards):
            for index, item in enumerate(board):
                if number == item:
                    row = int(index/5)
                    col = index%5
                    tracker[b_index][0][row] += 1
                    tracker[b_index][1][col] += 1

                    # subtract the number from the board sum
                    board_sum[b_index] -= number

        complete_board = np.argwhere(tracker==5)
        if complete_board.any():
            board_number = complete_board[0][0]
            return number * board_sum[board_number]

def get_last_winning_bingo_board(draw_list, boards):

    # create tracker array
    tracker = np.zeros((len(boards),2,5))
    board_sum = list(map(sum, boards))
    won_boards = set()

    for number in draw_list:
        for b_index, board in enumerate(boards):
            for index, item in enumerate(board):
                if number == item:
                    row = int(index/5)
                    col = index%5
                    tracker[b_index][0][row] += 1
                    tracker[b_index][1][col] += 1

                    # subtract the number from the board sum
                    board_sum[b_index] -= number

        complete_board = np.argwhere(tracker==5)
        if complete_board.any():
            for b in complete_board:
                if b[0] not in won_boards:
                    board_number = b[0]
                    won_boards.add(b[0])

            if len(won_boards) == len(boards):
                return number * board_sum[board_number]

if __name__ == '__main__':
    file = open('4-input.txt', 'r')
    #lines = [line.strip() for line in file.readlines()]

    boards = []
    index = -1
    # read draw_list and boards
    for line in file.readlines():

        if ',' in line:
            draw_list = [int(i) for i in line.strip().split(',')]
        elif line == '\n':
            index += 1
            boards.append([])
        else:
            row = [int(i) for i in line.strip().split(' ') if i !='']
            boards[index].extend(row)

    score = get_winning_bingo_board(draw_list, boards)

    print("Answer to first puzzle: ", score)

    score = get_last_winning_bingo_board(draw_list, boards)
    print("Answer to second puzzle: ", score)