from collections import Counter, namedtuple
import math

Univers = namedtuple("Univers", ['p1', 's1', 'p2', 's2'])

def get_place_on_board(move):

    return move if move <= 10 else move % 10

def get_n_scores(pos, rolls, n):

    move = pos + rolls[0]
    moves = [get_place_on_board(move)]

    for i in range(1, n):
        move += rolls[i%5]
        move = get_place_on_board(move)
        moves.append(move)

    return moves

def play_turn_for_univers(univers, u_nb, turn):
    """
    Every turn the dice rolls 3 times, hence creating 27 universes per branch
    """
    univers_moves_per_turn = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9:1}
    result = {}

    for move, univers_nb in univers_moves_per_turn.items():
        if turn % 2 == 1:
            if univers.s1 < 21:
                pos = get_place_on_board(univers.p1 + move)
                new_univers = Univers(pos, pos + univers.s1, univers.p2, univers.s2)
                result[new_univers] = univers_nb*u_nb
        else:
            if univers.s2 < 21:
                pos = get_place_on_board(univers.p2 + move)
                new_univers = Univers(univers.p1, univers.s1, pos, pos + univers.s2)
                result[new_univers] = univers_nb*u_nb

    return result

def play_turn_all_universes(univers_counter, turn):

    win1 = 0
    win2 = 0
    new_universes = Counter()

    for univers, u_nb in univers_counter.items():
        if turn % 2 == 1:
            if univers.s2 < 21:                
                new_universes += Counter(play_turn_for_univers(univers, u_nb, turn))
            else:         
                win2 += u_nb
        else:
            if univers.s1 < 21:
                new_universes += Counter(play_turn_for_univers(univers, u_nb, turn))
            else:
                win1 += u_nb

    return new_universes, win1, win2

if __name__ == '__main__':
    file = open('21-input.txt', 'r')
    lines = [line.strip() for line in file.readlines()]   

    pos1 = int(lines[0][-1])
    pos2 = int(lines[1][-1])
    print(pos1, pos2)

    win_score = 1000 
    rolls1 = [6, 4, 2, 0, 8]
    rolls2 = [5, 3, 1, 9, 7]

    moves1 = get_n_scores(pos1, rolls1, n = 5)
    moves2 = get_n_scores(pos2, rolls2, n = 10)

    cycle1 = sum(moves1)*2
    cycle2 = sum(moves2)

    if cycle1 > cycle2:
        win_cycle, lose_cycle = (cycle1, cycle2)
        win_moves, lose_moves = (moves1, moves2)
        ln, wn = (10, 5)
    else:
        win_cycle, lose_cycle = (cycle2, cycle1)
        win_moves, lose_moves = (moves2, moves1)
        ln, wn = (5, 10)

    turns = math.floor(win_score/win_cycle)
    win_score = turns*win_cycle
    lose_score = turns*lose_cycle

    turns = turns*10
    index = 0
    while win_score < 1000:
        win_score += win_moves[turns%wn]
        lose_score += lose_moves[turns%ln]
        turns += 1

    if cycle1 > cycle2:
        rolls = (turns-1)*6+3
        lose_score -= lose_moves[(turns-1)%ln]
    else:
        rolls = (turns-1)*6

    print("Answer to first puzzle: ", rolls*lose_score)
    
    win1 = 0
    win2 = 0

    initial_univers = Univers(pos1, 0, pos2, 0)
    initial_univers_counter = Counter()
    initial_univers_counter[initial_univers] = 1

    turn_dict = initial_univers_counter.copy()
    turn = 1
    while turn_dict:
        turn_dict, w1, w2 = play_turn_all_universes(turn_dict, turn)
        turn += 1
        win1 += w1
        win2 += w2

    print(win1, win2)
    print("Answer to second puzzle:", max(win1, win2))