def get_most_common_bit_per_position(lines):
    
    count = []
    for index, line in enumerate(lines):
        if index == 0:
            count = [0] *(len(line.strip())) 
        for i, val in enumerate(line.strip()):
            count[i] += int(val)

    gamma = [1 if i > index/2 else 0 for i in count]
    epsilon = [abs(i-1) for i in gamma]

    return gamma, epsilon

def convert_list_to_int(binary_list):
    x = 0
    for i in binary_list:
        x = (x << 1) | i

    return x

def convert_binary_string_to_list(s):
    return [int(i) for i in s.strip()]

if __name__ == '__main__':
    file_name = '3-input.txt'
    file = open(file_name, 'r')
    lines = file.readlines()
    
    g, e = get_most_common_bit_per_position(lines)
    g = convert_list_to_int(g)
    e = convert_list_to_int(e)

    print("Answer to first puzzle: ", g*e)

    positions = len(lines[0].strip())
    lines_g = lines.copy()
    lines_e = lines.copy()

    for i in range(0, positions):
        g = get_most_common_bit_per_position(lines_g)[0]

        if len(lines_g) > 1:
            lines_g = [line for line in lines_g if int(line[i]) == g[i]]
        
        e = get_most_common_bit_per_position(lines_e)[1]
        if len(lines_e) > 1:
            lines_e = [line for line in lines_e if int(line[i]) == e[i]]

    o2_rating = convert_binary_string_to_list(lines_g[0])
    o2_rating = convert_list_to_int(o2_rating)
    co2_rating = convert_binary_string_to_list(lines_e[0])
    co2_rating = convert_list_to_int(co2_rating)

    print("Answer to second puzzle: ", o2_rating * co2_rating)