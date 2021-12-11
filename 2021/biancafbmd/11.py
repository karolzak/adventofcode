import numpy as np

def step_progression(grid):

    flash_state = np.where(grid > 9)

    while len(flash_state[0]):
        adder = np.zeros((12, 12))
        for i,j in zip(*flash_state):
            np.add.at(adder[i], [j, j+1, j+2], 1)
            np.add.at(adder[i+1], [j, j+2], 1)
            np.add.at(adder[i+2], [j, j+1, j+2], 1)
        grid = np.where(grid > 9, -1000, grid)
        grid += adder[1:11, 1:11]
        flash_state = np.where(grid > 9)

    return np.where(grid < 0, 0, grid)

def get_step_all_flash(grid):
    
    step_add = np.ones((10, 10))
    step = 0

    while True:
        step +=1
        grid = step_progression(grid + step_add)
        
        if np.array_equal(grid, np.zeros((10, 10))):
            return step

def count_flashes(grid, steps):
    
    step_add = np.ones((10, 10))
    flashes = 0

    for i in range(0, steps):
        grid = step_progression(grid + step_add)
        flashes += len(np.argwhere(grid==0))

    return flashes

if __name__ == '__main__':
    file = open('11-input.txt', 'r')
    lines = [line.strip() for line in file.readlines()]
    
    grid = np.array([[int(char) for char in line] for line in lines])

    print("Answer to first puzzle: ", count_flashes(grid, 100))

    print("Answer to second puzzle: ", get_step_all_flash(grid))