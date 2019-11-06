#Copy-right: Frank Hu
#This code aims to extract the concealed messages
from cv2 import cv2

#Extract values from the least significant bit plane
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