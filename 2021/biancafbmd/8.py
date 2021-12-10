def decode_pattern(pattern):

    decoded = {}
    digits = pattern[0].split(' ')
    d8 = set('abcdefg')
    dce = set()

    for digit in digits:
        if len(digit) == 2:
            d1 = set(digit)
        elif len(digit) == 3:
            d7 = set(digit)
        elif len(digit) == 4:
            d4 = set(digit)
        elif len(digit) == 6:
            dce.update(set(digit) ^ d8)

    bd = d1 ^ d4
    decoded['a'] = d1 ^ d7
    eg = (d8 ^ d4) - decoded['a']
    decoded['d'] = bd & dce
    decoded['b'] = bd ^ decoded['d']
    decoded['c'] = dce & d1
    decoded['f'] = d1 - decoded['c']
    decoded['e'] = dce ^ decoded['c'] ^ decoded['d']
    decoded['g'] = eg - decoded['e']

    decoded = {min(v): k for k, v in decoded.items()}

    outputs = []
    for digit in pattern[1].split(' '):
        char_digits = sorted([decoded[c] for c in digit])
        outputs.append(''.join(char_digits))

    return outputs

def get_count_unique_digit(s):
    unique = [2, 3, 4, 7]

    return sum(1 for digit in s.split(' ') if len(digit) in unique)

if __name__ == '__main__':
    file = open('8-input.txt', 'r')
    lines = file.readlines()
    output_digits = [line.strip().split(' | ')[1] for line in lines]
    unique_digits = sum([get_count_unique_digit(digit) for digit in output_digits])

    print("Answer to first puzzle: ", unique_digits)

    digit_dict = {'abcefg': 0,  
                  'cf': 1,
                  'acdeg': 2,
                  'acdfg': 3,
                  'bcdf': 4,
                  'abdfg': 5,
                  'abdefg': 6,
                  'acf': 7,
                  'abcdefg': 8,
                  'abcdfg': 9}
    
    patterns = [line.strip().split(' | ') for line in lines]
    output_sum = 0

    for pattern in patterns:
        l = decode_pattern(pattern)
        number = digit_dict[l[0]]*1000 + \
                digit_dict[l[1]]*100 + \
                digit_dict[l[2]]* 10 + \
                digit_dict[l[3]]
        output_sum += number

    print("Answer to second puzzle: ", output_sum)