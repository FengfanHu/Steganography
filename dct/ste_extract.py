#Copy-right: Frank Hu
from cv2 import cv2
import numpy as np
import ste_embed as embed

#Main feature
#Extract the water print to original image
def extract_img(e_img, o_img, wp_row, wp_column):
    #Resize the origianl image to make the size match the format of 8N*8N
    o_img = embed.img_resize(o_img)
    #Split the original image and the embeded image
    o_blocks,_,_ = embed.img_split(o_img)
    e_blocks,_,_ = embed.img_split(e_img)
    #Get DCT blocks
    o_dct_blocks = embed.blocks_dct(o_blocks)
    e_dct_blocks = embed.blocks_dct(e_blocks)

    wp_size = wp_column * wp_column
    #Main feature
    blocks = []
    for i in range(wp_size):
        value = e_dct_blocks[i][7][7] - o_dct_blocks[i][7][7]
        blocks.append(value / embed.factor)
    #Make the blocks-array to image-array
    wp_img = np.array(blocks, dtype=np.uint8)
    wp_img = wp_img.reshape(wp_row, wp_column)
    return wp_img


if __name__ == "__main__":
    e_img = cv2.imread("../src/dct/embeded.bmp", cv2.IMREAD_GRAYSCALE)
    o_img = cv2.imread("../src/dct/original_img.bmp", cv2.IMREAD_GRAYSCALE)
    water_print = cv2.imread("../src/dct/waterprint.jpg", cv2.IMREAD_GRAYSCALE)
    
    wp_row = water_print.shape[0]
    wp_column = water_print.shape[1]

    wp_img = extract_img(e_img, o_img, wp_row, wp_column)

    cv2.imwrite("../src/dct/extracted_img.png", wp_img)
    cv2.imshow('wp_img', wp_img)
    k = cv2.waitKey(0)
    #ESC Catch event
    if k == 27:
        cv2.destroyAllWindows()