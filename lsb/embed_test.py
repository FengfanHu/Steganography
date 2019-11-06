from cv2 import cv2
import ste_embed
import ste_extract

img1 = cv2.imread("../src/original.bmp", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("../src/embedded.bmp", cv2.IMREAD_GRAYSCALE)
obit_stream = ste_embed.read_file("../src/data.txt")

print(obit_stream)
ebit_stream = ste_extract.extract_lsb(img2, len(obit_stream))
print("========分隔符========")
print(ebit_stream)

# for i in range(16):
#     img1_value = img1.item(0,i)
#     img2_value = img2.item(0,i)
#     print(i, "Original:", img1_value, "Embedded:", img2_value)