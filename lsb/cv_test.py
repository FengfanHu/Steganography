from cv2 import cv2
from matplotlib import pyplot as plt

#读取灰度图像 返回numpy.uint8
img = cv2.imread("../src/original.bmp", cv2.IMREAD_GRAYSCALE)
#读取RGB图像 返回numpy.ndarray
# img = cv2.imread("../original.png", cv2.IMREAD_COLOR)

#获取 灰度值
grey_value = img[0,0]
grey_value2 = img.item(0,0)

print("Value1:",grey_value, "Value2:",grey_value2)

#修改 灰度值
img.itemset((0,0),100)
print(img.item(0,0))
cv2.imwrite("../src/output2.bmp", img)

#图像 shape & 尺寸 0-Rows 1-Columns
shape = img.shape
size = img.size

print("Height:", img.shape[0])
print("Weight:", img.shape[1])

if img.shape[0] * img.shape[1] == size:
    print("As you wish, the result is right.")

#Datatype (which is important while debugging)
print("Datatype:", img.dtype)

#显示 图像
cv2.imshow('img', img)
k = cv2.waitKey(0)

#ESC 捕捉事件
if k == 27:
    cv2.destroyAllWindows()


