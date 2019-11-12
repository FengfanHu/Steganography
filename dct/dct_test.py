from cv2 import cv2
import ste_embed as embed

def dec2bit(grey_value):
    str = '{:0>15b}'.format(grey_value)
    return str

# water_print = cv2.imread("../src/dct/waterprint.png", cv2.IMREAD_GRAYSCALE)
# print_size = water_print.size
# #The preceding 15 bits are used for record the size of water print
# #So it's suitable for image smaller than 32768 bits
# size = dec2bit(print_size)
# print(size)
# print(type(size))
# print(int(size[0]))

img = cv2.imread("../src/dct/waterprint.jpg", cv2.IMREAD_GRAYSCALE)
for i in range(10):
    print(img.item(0,i))

# cv2.imshow('waterprint', img)
# k = cv2.waitKey(0)
# #ESC Catch event
# if k == 27:
#     cv2.destroyAllWindows()
# print(img.size)


