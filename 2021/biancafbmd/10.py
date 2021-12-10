from collections import Counter
import statistics as st

def find_first_illegal_char(line):

    chunk = {')': '(', ']': '[', '>': '<', '}': '{'}
    working_list = []

    for char in line:
        if char in chunk.keys():
            if chunk[char] == working_list[-1]:
                working_list.pop()
            else:
                return char
        else:
            working_list.append(char)

def complete_line_and_get_score(line):

    chunk = {')': '(', ']': '[', '>': '<', '}': '{'}
    score_table = {'(': 1, '[': 2, '{': 3, '<': 4}
    working_list = []

    for char in line:
        if char in chunk.keys():
            if chunk[char] == working_list[-1]:
                working_list.pop()
            else:
                return
        else:
            working_list.append(char)

    score = 0
    while working_list:
        score = score*5 + score_table[working_list.pop()]
    
    return score

if __name__ == '__main__':
    file = open('10-input.txt', 'r')
    lines = file.readlines()

    score = {')': 3, ']': 57, '}': 1197, '>': 25137}

    illegal_chars = Counter([find_first_illegal_char(line.strip()) for line in lines])
    del illegal_chars[None]

    syntax_error_score = sum([v*score[k] for k, v in illegal_chars.items()])

    print("Answer to first puzzle: ", syntax_error_score)

    scores = [complete_line_and_get_score(line.strip()) for line in lines]
    scores = [s for s in scores if s]

    print("Answer to second puzzle: ", st.median(scores))