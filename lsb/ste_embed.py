#Copy-right: Frank Hu
#This code aims to use least significant bit plane to conceal messages
from cv2 import cv2
import random

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

#LSB process
#The value of the least significant bit plane can be simply get by complementing 2
def lsb_process(img, bit_stream):
    count = 0   #Caculator
    img_rows = img.shape[0]
    img_columns = img.shape[1]

    for row in range(img_rows):
        for column in range(img_columns):
            pixel_value = img.item(row, column)
            lsb_pixel_value = pixel_value % 2
            #String and int are never allowed to match without transforming
            if lsb_pixel_value != int(bit_stream[count]):
                img.itemset((row,column), pixel_value + 1)
            count += 1  #Caculator + 1

if __name__ == "__main__":
    #Use grey-scale to read image
    img = cv2.imread("../src/original.bmp", cv2.IMREAD_GRAYSCALE)
    #Transform file data to bit-stream
    bit_stream = read_file("../src/data.txt")
    #Image size which equals to rows * columns
    img_size = img.size
    #Sub-length is used to fill the bit-stream
    sub_length = img_size - len(bit_stream)

    if sub_length < 0:
        print("There is a data overflow, your action has been forbiddened.")
        exit()

    #Fill the bit-stream to match the length of size of image
    for _ in range(sub_length):
        bit_stream += random.sample('01',1)[0]

    #LSB process
    lsb_process(img, bit_stream)
    
    cv2.imwrite("../src/embedded.bmp", img)
    print("Message embedded successfully.")