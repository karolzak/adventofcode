import statistics as st
import math

def get_fuel_for_position(positions, best_pos):

    fuel = [abs(best_pos - x)*(abs(best_pos - x)+1)/2 for x in positions]
    return sum(fuel)

if __name__ == '__main__':
    file = open('7-input.txt', 'r')
    lines = file.readlines()

    pos = [int(x) for x in lines[0].split(',')]

    best_pos = st.median(pos)
    fuel = sum([abs(best_pos - x) for x in pos])

    print("Answer to first puzzle: ", fuel)

    best_pos1 = math.ceil(st.mean(pos))
    best_pos2 = math.floor(st.mean(pos))
    fuel1 = get_fuel_for_position(pos, best_pos1)
    fuel2 = get_fuel_for_position(pos, best_pos2)

    print("Answer to second puzzle: ", min(fuel1, fuel2))