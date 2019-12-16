#This code aims to extract the concealed messages
from cv2 import cv2
import numpy as np
import json

def random_recover(bit_stream):
    '''
    Recoverign the random bit stream
    '''
    with open('../src/random.json', mode="r") as file:
        index_list = json.load(file)
    new_bit_stream = [0 for _ in range(len(index_list))]
    for count, index in enumerate(index_list):
        new_bit_stream[index] = bit_stream[count]
    return ''.join(new_bit_stream)

def bit_streamRecovering(bit_stream, flag):
    '''
    Recovering the normalized bit stream.
    Pay a attention to the Arg: flag
    @return bit_stream
    '''
    with open('../src/index.json', mode="r") as file:
        index_list = json.load(file)
    if flag:
        for index in index_list:
            bit_stream = bit_stream[:index]+'1'+bit_stream[index+1:]
    else:
        for index in index_list:
            bit_stream = bit_stream[:index]+'0'+bit_stream[index+1:]
    return bit_stream

'''
Extract values from the least significant bit plane
'''
def extract_lsb(img, length):
    count = 0
    bit_stream = ""
    img_rows = img.shape[0]
    img_columns = img.shape[1]
    for row in range(img_rows):
        for column in range(img_columns):
            if count == length:
                break
            lsb_pixel_value = img.item(row, column) % 2
            bit_stream += str(lsb_pixel_value)
            count += 1
        if count == length:
            break
    return bit_stream
    
#Transform bit-stream to str format
def bit_stream2str(bit_stream):
    bits_array = []
    msg = ""
    count = int(len(bit_stream)/8)
    for i in range(count):
        bits_array.append(int(bit_stream[0+8*i:8+8*i], 2))
    for i in range(len(bits_array)):
        msg += chr(bits_array[i])
    return msg

#Transform bit-stream to img(gray)
def bit_stream2gray_img(bit_stream, rows, columns):
    img_array = []
    count = int(len(bit_stream)/8)
    for i in range(count):
        img_array.append(int(bit_stream[0+8*i:8+8*i], 2))
    #Make the array to image-array
    wp_img = np.array(img_array, dtype=np.uint8)
    wp_img = wp_img.reshape(rows, columns)
    return wp_img

#Transform bit-stream to img(binary)
def bit_stream2binary_img(bitstream, rows, columns):
    count = len(bitstream)
    img_array = []
    for index in range(count):
        if bitstream[index] == '1':
            img_array.append(255)
        elif bitstream[index] == '0':
            img_array.append(0)
    wp_img = np.array(img_array, dtype=np.uint8)
    wp_img = wp_img.reshape(rows, columns)
    return wp_img