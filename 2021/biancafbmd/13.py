import numpy as np
import pprint

def construct_paper(dots):
    # x, y are inversed
    y_max = max([dot[0] for dot in dots])
    x_max = max([dot[1] for dot in dots])

    paper = np.zeros((x_max+1, y_max+1))
    
    for dot in dots:
        paper[dot[1]][dot[0]] = 1
    
    return paper

def fold_paper(paper, fold):
    
    if 'x' in fold:
        x = int(fold.split('=')[1])
        result = paper[:, 0:x]
        x_diff = 2*x - paper.shape[1] + 1

        flipped = np.flip(paper[:, x+1:], 1)
        result[:, x_diff:x] = result[:, x_diff:x] + flipped
        return result
    elif 'y' in fold:
        y = int(fold.split('=')[1])
        result = paper[0:y, :]
        y_diff = 2*y - paper.shape[0] + 1

        flipped = np.flip(paper[y+1:, :], 0)
        result[y_diff:y, :] = result[y_diff:y, :] + flipped
        return result


if __name__ == '__main__':
    file = open('13-input.txt', 'r')
    lines = [line.strip() for line in file.readlines()]   

    dots = [[int(x) for x in line.split(',')] for line in lines if ',' in line]
    paper = construct_paper(dots)    

    # extract folds
    expr = 'fold along '
    folds = [line.split(expr)[1] for line in lines if expr in line]
    
    p1 = fold_paper(paper, folds[0])
    print("Answer to first puzzle: ", np.count_nonzero(p1))

    folded = paper.copy()
    for fold in folds:
       folded = fold_paper(folded, fold)
    
    index = int(folded.shape[1]/2)
    # print the output to be able to read the letters
    print([['#' if i>0 else '.' for i in line[0:index]] for line in folded])
    print([['#' if i>0 else '.' for i in line[index:]] for line in folded])
    print("Answer to second puzzle: EAHKRECP")