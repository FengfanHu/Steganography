from cv2 import cv2
import math

o_water_print = cv2.imread("../src/dct/waterprint.jpg", cv2.IMREAD_GRAYSCALE)
e_water_print = cv2.imread("../src/dct/extracted_img.png", cv2.IMREAD_GRAYSCALE)
o_image = cv2.imread("../src/dct/original_img.bmp", cv2.IMREAD_GRAYSCALE)
e_image = cv2.imread("../src/dct/embeded.bmp", cv2.IMREAD_GRAYSCALE)


wp_rows = o_water_print.shape[0]
wp_columns = o_water_print.shape[1]
img_rows = o_image.shape[0]
img_columns = o_image.shape[1]

wp_size = wp_columns * wp_rows
img_size = img_rows * img_columns

wp_MSE = 0
for row in range(wp_rows):
    for column in range(wp_columns):
        temp_value = e_water_print.item(row, column) - o_water_print.item(row, column)
        wp_MSE += math.pow(temp_value, 2)

wp_MSE /= wp_size
print("wp_MSE:", wp_MSE)

wp_value = math.pow(255, 2)/wp_MSE
wp_PNSR = 10 * math.log(wp_value ,10)
print("wp_PSNR:", wp_PNSR)

img_MSE = 0
for row in range(img_rows):
    for column in range(img_columns):
        temp_value = e_image.item(row, column) - o_image.item(row, column)
        img_MSE += math.pow(temp_value, 2)

img_MSE /= img_size
print("img_MSE:", img_MSE)

img_value = math.pow(255, 2)/img_MSE
img_PNSR = 10 * math.log(img_value ,10)
print("img_PSNR:", img_PNSR)




