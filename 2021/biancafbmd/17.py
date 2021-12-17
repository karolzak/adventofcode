import math

def get_x_step_candidates(tx_min, tx_max, step_max):

    l_x = math.ceil(math.sqrt(2*tx_min + 0.25) - 0.5)
    u_x = math.floor(math.sqrt(2*tx_max + 0.25) - 0.5)

    candidates = set()

    for x in range(l_x, u_x+1):
        for step in range(x, step_max):
            candidates.add((x, step))
    

    for step in range(1, l_x+1):
        l_x = math.ceil(tx_min/step + (step-1)/2)
        u_x = math.floor(tx_max/step + (step-1)/2)

        for y in range(l_x, u_x+1):
            candidates.add((y, step))

    return candidates            

def get_max_step(tx_max):

    return tx_max*2 + 1

def get_position(xv_0, yv_0, step):

    if step < xv_0:
        xv_n = step*(xv_0 - (step-1)/2)
    else:
        xv_n = xv_0*(xv_0+1)/2
    yv_n = step*(yv_0 - (step-1)/2)

    return xv_n, yv_n

def get_y_step_candidates(ty_min, ty_max, step_max):

    candidates = set()

    for step in range(1, step_max):
        l_y = math.ceil(ty_min/step + (step-1)/2)
        u_y = math.floor(ty_max/step + (step-1)/2)

        for y in range(l_y, u_y+1):
            candidates.add((y, step))
    
    return candidates


def match_candidates(x_steps, y_steps):

    candidates = set()

    for y, y_step in y_steps:
        for x, x_step in x_steps:
            if x_step == y_step:
                candidates.add((x, y))
    
    return candidates


if __name__ == '__main__':
    file = open('17-input.txt', 'r')
    lines = [line.strip() for line in file.readlines()]   

    target_x1, target_x2 = [int(i) for i in lines[0].split('x=')[1].split(',')[0].split('..')]
    target_y1, target_y2 = [int(i) for i in lines[0].split('y=')[1].split('..')]
    tx_min, tx_max = min(target_x1, target_x2), max(target_x1, target_x2)
    ty_min, ty_max = min(target_y1, target_y2), max(target_y1, target_y2)

    step_max = get_max_step(tx_max)
    
    y_candidates = get_y_step_candidates(ty_min, ty_max, step_max)

    y0 = max(y_candidates)[0]
    max_y_val = y0*(y0+1)/2

    print("Answer to first puzzle: ", max_y_val)  

    x_candidates = get_x_step_candidates(tx_min, tx_max, step_max)

    candidates = match_candidates(x_candidates, y_candidates)

    print("Answer to second puzzle:", len(candidates))