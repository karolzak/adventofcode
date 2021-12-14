from collections import Counter, defaultdict
import numpy as np
import time

def get_rules_dict(lines):
    
    return {k:v for line in lines for k, v in [line.split(' -> ')]}

def construct_matrix_from_input(lines):
    """
    Construct matrix for 1 step process from lines

    :param lines: list of lines containing the process rules
            'AB' -> B' inserts will lead to 'ABB' 

    :return: matrix, dict_mapping 

    ------
    Example: 
    the process AB -> B, BB -> A, BA -> A, AA -> B
    is mapped to the following process matrix
      |AB|BB|BA|AA
    AB| 1| 1| 0| 0
    BB| 1| 0| 1| 0
    BA| 0| 0| 1| 1
    AA| 1| 0| 1| 0

    with dict_mapping = {'AB': 0, 'BB': 1, 'BA': 2, 'AA': 3}
    ------
    """
    rules_dict = {k:[k[0]+v,v+k[1]] for line in lines for k, v in [line.split(' -> ')]}
    m_len = len(rules_dict)
    rules_matrix = np.zeros((m_len, m_len))

    dict_mapping = {pair: i for i, pair in enumerate(rules_dict)}
    
    for pair, inserts in rules_dict.items():
        x = dict_mapping[pair]
        y0 = dict_mapping[inserts[0]]
        y1 = dict_mapping[inserts[1]]
        rules_matrix[x, y0] += 1
        rules_matrix[x, y1] += 1
    
    return rules_matrix, dict_mapping

def get_polymer_result(template, rules, steps):

    for step in range(0, steps):
        n_temp = ''
        tem_len = len(template) -1

        for i in range(0, tem_len):
            chars = template[i:i+2]
            n_temp = n_temp + chars[0] + rules[chars]

        template = n_temp + template[tem_len]

    return template

def calculate_counts(template, start_template, dict_mapping):

    counts = defaultdict(int)
    counts[start_template[0]] = -1/2
    counts[start_template[-1]] = -1/2

    for pair in dict_mapping:
        index = dict_mapping[pair]
        counts[pair[0]] += template[index]/2
        counts[pair[1]] += template[index]/2

    counts[start_template[0]] += 1
    counts[start_template[-1]] +=1

    return counts

if __name__ == '__main__':
    file = open('14-input.txt', 'r')
    lines = [line.strip() for line in file.readlines()]   

    template = lines[0]
    rules = get_rules_dict(lines[2:])

    pol_counts = Counter(get_polymer_result(template, rules, 10)).most_common()

    print("Answer to first puzzle: ", pol_counts[0][1] - pol_counts[-1][1])

    rules_matrix, dict_mapping = construct_matrix_from_input(lines[2:])
    template_list = [template[i:i+2] for i in range(0, len(template)-1)]
    
    template_vector = np.zeros((len(dict_mapping)))
    for pair in template_list:
        template_vector[dict_mapping[pair]] += 1

    n_steps = 40

    start_time = time.time()
    for i in range(0, n_steps):
        template_vector = np.matmul(template_vector,rules_matrix)

    counts = calculate_counts(template_vector, template, dict_mapping)
    print("Answer to second puzzle:", max(counts.values())-min(counts.values()))

    print("time taken for part 2", time.time()- start_time)