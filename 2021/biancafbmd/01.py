def count_increased(measures):
    count = 0
    current = measures[0]

    for measure in measures:
        if (current - measure) < 0:
            count +=1
        current = measure
    return count

def count_sliding_window(measures, window_length=3):
    n = len(measures)
    count = 0

    for i in range(0, n-window_length):
        if (measures[i] - measures[i+window_length]) < 0:
            count +=1

    return count

if __name__ == '__main__':
    file1 = open('1-input.txt', 'r')
    lines = file1.readlines()
    lines = [int(l.strip()) for l in lines]

    print("Answer to first puzzle: ", count_increased(lines))
    print("Answer to second puzzle: ", count_sliding_window(lines))
