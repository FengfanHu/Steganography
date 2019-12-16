from cv2 import cv2
import ste_embed

img = cv2.imread("../src/dct/original.bmp", cv2.IMREAD_GRAYSCALE)
img = ste_embed.img_resize(img)
cv2.imwrite("../src/dct/original_img.bmp", img)