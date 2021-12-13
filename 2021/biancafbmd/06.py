from collections import deque, Counter

def simulate_fish(state, day, end_day):

    if day == end_day:
        return len(state)

    else:
        for i in range(0, len(state)):
            if state[i] == 0:
                state[i] = 6
                state.append(8)
            else:
                state[i] -= 1

        return simulate_fish(state, day+1, end_day)

def count_fish(state, days):

    fish_count = deque([state.count(i) for i in range(0, 9)])

    for day in range(0, days):
        fish_count.rotate(-1)
        fish_count[6] += fish_count[8]

    return sum(fish_count)

if __name__ == '__main__':
    file = open('6-input.txt', 'r')
    lines = file.readlines()

    ages = [int(x) for x in lines[0].split(',')]

    print("Answer to first puzzle: ", simulate_fish(ages.copy(), 0, 80))

    print("Answer to second puzzle: ", count_fish(ages, 256))