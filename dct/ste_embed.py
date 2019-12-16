#Copy-right: Frank Hu
from cv2 import cv2
import numpy as np

#Resize the image to a format like 8N*8N
def img_resize(img):
    img_rows = img.shape[0] // 8 * 8
    img_columns = img.shape[1] // 8 * 8
    img = cv2.resize(img, (img_columns, img_rows))
    return img

#Split the image-array to a list of block(8*8)
def img_split(img):
    blocks = []
    img_rows = img.shape[0]
    img_columns = img.shape[1]
    #Make the values of both rows-number and columns-number to 8N
    row_count =  img_rows // 8
    column_count = img_columns // 8
    #Assign the values of image to each block
    for row_c in range(row_count):
        for col_c in range(column_count):
            temp = np.zeros((8, 8), dtype=np.float)
            for row in range(8):
                for col in range(8):
                    temp[row][col] = img.item(row+row_c*8, col+col_c*8)
            blocks.append(temp)
    return blocks, column_count, row_count

#Have each block DCT
def blocks_dct(blocks):
    dct_blocks = []
    for blocks_no in range(len(blocks)):
        dct_block = cv2.dct(blocks[blocks_no])
        dct_blocks.append(dct_block)
    return dct_blocks

#Main feature
#Embed the water print to original image
#If embed the value 0 then do the following operations, it will be unpredictable
factor = 0.05
#You should pay attention to the factor, it depends the quality of embeded image
#and the water print extracted.
#Here we just set the factor 0.05
def embed_img(dct_blocks, water_print):
    wp_column = water_print.shape[1]
    wp_size = water_print.size
    bks_size = len(dct_blocks)
    if bks_size < wp_size:
        print("There is a data overflow, your action has been forbiddened.")
        exit()
    #The value of water print can not be embedded straightly
    for i in range(wp_size):
        row = i//wp_column
        column = i%wp_column
        dct_blocks[i][7][7] += factor * water_print.item(row, column)
    return dct_blocks

#Have each block IDCT
def blocks_idct(dct_blocks):
    idct_blocks = []
    for blocks_no in range(len(dct_blocks)):
        idct_block = cv2.idct(dct_blocks[blocks_no])
        idct_blocks.append(idct_block)
    return idct_blocks

#Merge the blocks to image-array
def blocks2img(blocks, row_count, column_count):
    new_blocks = []
    for row_c in range(row_count):
        for row_no in range(8):
            temp = []
            for col_c in range(column_count):
                #Choose a block
                block = blocks[row_c*column_count + col_c]
                temp.extend(block[row_no])
            new_blocks.append(temp)
    return np.array(new_blocks, dtype=np.uint8)


if __name__ == "__main__":
    #Read image by grayscale way.
    img = cv2.imread("../src/dct/original_img.bmp", cv2.IMREAD_GRAYSCALE)
    water_print = cv2.imread("../src/dct/waterprint.jpg", cv2.IMREAD_GRAYSCALE)
    #Resize the image to a format like 8N*8N
    new_img = img_resize(img)   # 228*150 = 34200
    #Split the image to a list of block(8*8)
    blocks, column_count, row_count = img_split(new_img) 
    #DCT blocks
    dct_blocks = blocks_dct(blocks) #The type of value must be float in dct.
    #Embed the water print
    dct_blocks = embed_img(dct_blocks, water_print)
    #IDCT blocks
    idct_blocks = blocks_idct(dct_blocks)
    #Merge the blocks to image-array 
    new_img = blocks2img(idct_blocks, row_count, column_count)
    cv2.imwrite("../src/dct/embeded.bmp", new_img)

    cv2.imshow('embeded_img', new_img)
    k = cv2.waitKey(0)
    #ESC Catch event
    if k == 27:
        cv2.destroyAllWindows()
