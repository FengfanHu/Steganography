from cv2 import cv2
import ste_embed
import ste_extract

# img1 = cv2.imread("../src/lsb/original.bmp", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("../src/lsb/embedded.bmp", cv2.IMREAD_GRAYSCALE)

#Extract watermark.
ebit_stream = ste_extract.extract_lsb(img2, 65536)

ebit_stream = ste_extract.random_recover(ebit_stream)

ebit_stream = ste_extract.bit_streamRecovering(ebit_stream, 1)

'''
Extract gray-type water mark.
'''
# img = ste_extract.bit_stream2gray_img(ebit_stream, 90, 90)
'''
Extract binary-type water mark.
'''
img = ste_extract.bit_stream2binary_img(ebit_stream, 256, 256)
cv2.imshow('watermark', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()

# for i in range(16):
#     img1_value = img1.item(0,i)
#     img2_value = img2.item(0,i)
#     print(i, "Original:", img1_value, "Embedded:", img2_value)

