import numpy as np
from collections import defaultdict

from numpy.lib.arraypad import pad

def enhance_image(image, algo, padder = '.'):

    x, y = image.shape
    pad_offset = 1
    pad_image = np.pad(image, pad_offset+1, pad_with, padder=padder)
    enhanced = np.pad(image, pad_offset, pad_with, padder=padder)

    for i in range(0, x+pad_offset+1):
        for j in range(0, y+pad_offset+1):
            #print(i, j, get_position_for_pixel(pad_image, (i+pad_offset, j+pad_offset)))
            enhanced[i, j] = algo[get_position_for_pixel(pad_image, (i+pad_offset, j+pad_offset))]

    return enhanced

def image_to_dec(image_string):

    binary_string = ''.join(['1' if char=='#' else '0' for char in image_string])
    return int(binary_string, 2)

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', '.')
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value

def get_position_for_pixel(image, pixel):

    x, y = pixel
    extracted_pixels = image[x-1:x+2, y-1:y+2].flatten()

    image_string = ''.join(extracted_pixels)

    return image_to_dec(image_string)


if __name__ == '__main__':
    file = open('20-input.txt', 'r')
    lines = [line.strip() for line in file.readlines()]   

    image_enh = lines[0]
    image = np.array([[char for char in line] for line in lines[2:]])
    
    enh1 = enhance_image(image, image_enh)
    if image_enh[0] == '#':
        enh2 = enhance_image(enh1, image_enh, padder='#')
    elif image_enh[0] == '.':
        enh2 = enhance_image(enh1, image_enh)

    print("Answer to first puzzle: ", np.count_nonzero(enh2 == '#')) 

    enh = np.copy(image)
    enh_steps = 50
    for step in range(0, enh_steps):
        if step % 2 == 0:
            enh = enhance_image(enh, image_enh)
        else:
            if image_enh[0] == '#':
                enh = enhance_image(enh, image_enh, padder='#')
            elif image_enh[0] == '.':
                enh = enhance_image(enh, image_enh)

    print("Answer to second puzzle:", np.count_nonzero(enh == '#'))