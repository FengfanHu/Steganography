#This code aims to use least significant bit plane to conceal messages
from cv2 import cv2
import random, math, json

#Resize the image to a format like 4N*4N
def img_resize(img):
    img_rows = img.shape[0] // 4 * 4
    img_columns = img.shape[1] // 4 * 4
    img = cv2.resize(img, (img_columns, img_rows))
    return img

#Dec to bit
#Since values are less than 255, so we use 8 bits.
def dec2bit(grey_value):
    str = '{:0>8b}'.format(grey_value)
    return str

#Read file
#Using bytes format to read file
def read_file(path):
    fp = open(path, "rb")
    msg = fp.read() #return byte-array
    bit_stream = ""
    for i in range(len(msg)):
        bit_stream += dec2bit(msg[i])
    fp.close()
    return bit_stream

#Water-print(gray) to bit_stream
def read_gray_img(img):
    rows = img.shape[0]
    columns = img.shape[1]
    values = []
    bit_stream = ''
    for row in range(rows):
        for column in range(columns):
            value = img.item(row, column)
            values.append(value)
    for value in values:
        temp = dec2bit(value)
        bit_stream += temp
    return bit_stream

#Water-print(Binary) to bit_stream
def read_binary_image(img):
    rows = img.shape[0]
    columns = img.shape[1]
    bit_stream = ''
    for row in range(rows):
        for column in range(columns):
            pixel_value = img.item(row, column)
            if pixel_value == 255:
                bit_stream += '1'
            elif pixel_value == 0:
                bit_stream += '0'
    return bit_stream

def zero_oneAssembling(bit_stream):
    '''
    Assemble the index of zero and one in a bit stream.
    @zero_list, @one_list
    '''
    one_list = [ index  for index,value in enumerate(bit_stream) if value == '1' ]
    zero_list = [ index for index,value in enumerate(bit_stream) if value == '0' ]
    return zero_list, one_list

def bit_streamAnalysing(bit_stream):
    '''
    Analyse the number of zero and one in a bit stream.
    @return zero_p
    @return one_p
    '''
    zero_list, one_list = zero_oneAssembling(bit_stream)
    length, one_count, zero_count = len(bit_stream), len(one_list), len(zero_list)
    zero_p, one_p = zero_count/length, one_count/length
    return zero_p, one_p

def bit_streamNormalizing(bit_stream):
    '''
    Normalize a bit stream, making the number of zero and one equal.
    @return bit_stream
    @return flag    Flag is used to recover the bit-stream
    '''
    zero_list, one_list = zero_oneAssembling(bit_stream)
    flag, diff = len(one_list) > len(zero_list), abs(len(one_list) - len(zero_list))//2
    if flag:
        index_list = [one_list[index] for index in random.sample(range(len(one_list)), diff)]
        for index in index_list:
            bit_stream = bit_stream[:index]+'0'+bit_stream[index+1:]
        with open('../src/index.json', mode='w+') as file:
            json.dump(index_list, file)
    else:
        index_list = [zero_list[index] for index in random.sample(range(len(zero_list)), diff)]
        for index in index_list:
            bit_stream = bit_stream[:index]+'1'+bit_stream[index+1:]
        with open('../src/index.json', mode='w+') as file:
            json.dump(index_list, file)
    return bit_stream, flag

def bit_streamRandoming(bit_stream):
    '''
    This function aims to prevent the visible attack.
    @return new_bit_stream
    '''
    index_list = [ index for index in random.sample(range(len(bit_stream)), len(bit_stream))]
    with open('../src/random.json', mode='w+') as file:
        json.dump(index_list, file)
    new_bit_stream = ''
    for index in index_list:
        new_bit_stream += bit_stream[index]
    return new_bit_stream

def lsb_process(img, bit_stream, depth=8, method=1):
    '''
    LSB process
    process-1: This method just simply swap the lsb value.
    process-2: If the index value changed, add 1.
    process-3: 1 -> 01 | 0 -> 00
    '''
    count = 0   #Caculator
    img_rows = img.shape[0]
    img_columns = img.shape[1]

    for row in range(img_rows):
        for column in range(img_columns):
            pixel_value = img.item(row, column)
            pixel_value_str = dec2bit(pixel_value)
            bit = bit_stream[count]
            if method == 1:
                swap_value = pixel_value_str[:depth-1]+bit+pixel_value_str[depth:]
                img.itemset((row,column), int(swap_value, 2))
            elif method == 2:
                index_value = pixel_value_str[depth-1]
                if index_value != bit:
                    img.itemset((row,column), (pixel_value + int(math.pow(2, 8-depth))))
            elif method == 3:
                index_value = pixel_value_str[depth-1]
                if bit == '0':
                    if index_value != bit:
                        swap_value = pixel_value_str[:depth-2]+'0'+'0'+pixel_value_str[depth:]
                        img.itemset((row,column), int(swap_value, 2))
                elif bit == '1':
                    if index_value != bit:
                        swap_value = pixel_value_str[:depth-2]+'0'+'1'+pixel_value_str[depth:]
                        img.itemset((row,column), int(swap_value, 2))
            count += 1  #Caculator + 1

if __name__ == "__main__":
    #Use grey-scale to read image
    img = cv2.imread("../src/lsb/lena.bmp", cv2.IMREAD_GRAYSCALE)

    #Transform watermark to bit-stream
    watermark = cv2.imread('../src/lsb/watermark.bmp', cv2.IMREAD_GRAYSCALE)

    # bit_stream = read_gray_img(waterprint)
    bit_stream = read_binary_image(watermark)

    #Image size which equals to rows * columns
    img_size = img.size
    #Sub-length is used to fill the bit-stream
    sub_length = img_size - len(bit_stream)

    if sub_length < 0:
        print("There is a data overflow, your action has been forbiddened.")
        exit()

    #Normalizing the bit stream
    # bit_stream, flag = bit_streamNormalizing(bit_stream)
    
    #Randoming the bit stream
    # bit_stream = bit_streamRandoming(bit_stream)

    #LSB process
    lsb_process(img, bit_stream, 8, 1)
    
    cv2.imwrite("../src/lsb/embedded.bmp", img)
    print("Message embedded successfully.")