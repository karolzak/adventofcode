import math

def decode_literal_val(bit_string, index=0):

    lit_val = ''
    group_len = 5
    prefix_bit = bit_string[index]

    # loop through all the bits starting with 1
    while prefix_bit!= '0':
        lit_val += bit_string[index+1: index+group_len]
        index = index+group_len
        prefix_bit = bit_string[index]

    # get the last part of the value
    lit_val += bit_string[index+1: index+group_len]
    lit_dec = int(lit_val, 2)
    index += group_len

    return index, lit_dec

def get_version_type_id(bit_string):
    index = 0
    packet_version = int(bit_string[index:index+3], 2)
    type_id = int(bit_string[index+3:index+6], 2)
    return packet_version, type_id
    
def decode_packet(bit_string, index = 0):

    packet_version_list = []
    packet_version, type_id = get_version_type_id(bit_string)
    packet_version_list.append(packet_version)
    index += 6

    if type_id == 4:
        index, lit_dec = decode_literal_val(bit_string, index)
        print("literal value", lit_dec)
        return index, packet_version_list, lit_dec

    else:
        print("operator", type_id)
        length_type_id = bit_string[index]
        index +=1
        values = []
        if length_type_id == '0':
            next_bits = 15
            sub_pack_len = int(bit_string[index: index+next_bits],2)
            index += next_bits
            print("op type 0 - subpack length ", sub_pack_len, index)

            while sub_pack_len > 0:
                i, versions, value = decode_packet(bit_string[index:])
                packet_version_list.extend(versions)
                index += i
                sub_pack_len -= i
                values.append(value)
                    
        else:
            next_bits = 11
            sub_pack_nb = int(bit_string[index: index+next_bits],2)
            print("op type 1 - number of subpackets ", sub_pack_nb)
            index += next_bits

            for step in range(0, sub_pack_nb):
                i, versions, value = decode_packet(bit_string[index:])
                packet_version_list.extend(versions)
                index += i 
                values.append(value) 

        if type_id == 0:
            value = sum(values)
        elif type_id == 1:
            value = math.prod(values)
        elif type_id == 2:
            value = min(values)
        elif type_id == 3:
            value = max(values)
        elif type_id == 5:
            value = 1 if values[0] > values[1] else 0
        elif type_id == 6:
            value = 1 if values[0] < values[1] else 0
        elif type_id == 7:
            value = 1 if values[0] == values[1] else 0

    print(type_id, values, value)
    return index, packet_version_list, value

def hex_to_binary(hex_string):

    expected_len = 4*len(hex_string)
    return str(bin(int(hex_string, 16))[2:].zfill(expected_len))

if __name__ == '__main__':
    file = open('16-input.txt', 'r')
    lines = [line.strip() for line in file.readlines()]   

    hex_string = hex_to_binary(lines[0])
    i, versions, value = decode_packet(hex_string)
        
    print("Answer to first puzzle: ", sum(versions))  

    print("Answer to second puzzle:", value)