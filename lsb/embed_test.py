from cv2 import cv2
import ste_embed
import ste_extract

# img1 = cv2.imread("../src/lsb/original.bmp", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("../src/lsb/embedded.bmp", cv2.IMREAD_GRAYSCALE)
# obit_stream = ste_embed.read_file("../src/lsb/data.txt")

# print(obit_stream)
# ebit_stream = ste_extract.extract_lsb(img2, len(obit_stream))
# print("========分隔符========")
# print(ebit_stream)
# msg = ste_extract.bit_stream2str(ebit_stream)
# print(msg)

ebit_stream = ste_extract.extract_lsb(img2, 64800)
img = ste_extract.bit_stream2img(ebit_stream, 90, 90)
cv2.imshow('watermark', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()

# for i in range(16):
#     img1_value = img1.item(0,i)
#     img2_value = img2.item(0,i)
#     print(i, "Original:", img1_value, "Embedded:", img2_value)


#RS
# def f1(value):
#   if value%2 == 0:
#     value += 1
#   else:
#     value -= 1
#   return value

# def f_1(value):
#   if value%2 == 0:
#     value -= 1
#   else:
#     value += 1
#   return value

# values = []
# for row in range(rows):
#   for column in range(columns):
#     value = img1.item(row, column)
#     values.append(value)

# valuesf1 = []
# for v in values:
#   value = f1(v)
#   valuesf1.append(value)

# valuesf_1 = []
# for v in values:
#   value = f_1(v)
#   valuesf_1.append(value)

# sub = []
# for i in range(len(values)):
#   value = valuesf1[i] - valuesf_1[i]
#   sub.append(value)

