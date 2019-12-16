from cv2 import cv2
import visible, histogram, random
from ste_embed import read_binary_image, bit_streamAnalysing, bit_streamNormalizing, bit_streamRecovering, bit_streamRandoming

if __name__ == "__main__":

  # img = cv2.imread('../src/lsb/waterprint.jpg', cv2.IMREAD_GRAYSCALE)
  # img = cv2.resize(img, (90,90))
  # cv2.imwrite('../src/lsb/wp.bmp', img)

  # img = cv2.imread('../src/lsb/lena.bmp', cv2.IMREAD_GRAYSCALE)
  # img2 = cv2.imread('../src/lsb/embedded.bmp', cv2.IMREAD_GRAYSCALE)
  # img3 = cv2.imread('../src/lsb/watermark.bmp', cv2.IMREAD_GRAYSCALE)
  # cv2.imshow('../src/lsb/original.bmp',img)
  # cv2.imshow('embedded',img2)
  # cv2.imshow('wm', img3)
  # k = cv2.waitKey(0)
  # if k == 27:
  #   cv2.destroyAllWindows()

  '''
  最低位平面
  '''
  # img = cv2.imread('../src/lsb/embedded.bmp', cv2.IMREAD_GRAYSCALE)
  # img = visible.lsb(img, 8)
  # cv2.imshow('test', img)
  # k = cv2.waitKey(0)
  # if k == 27:
  #   cv2.destroyAllWindows()

  '''
  提取水印
  '''
  img = cv2.imread('../src/lsb/embedded.bmp', cv2.IMREAD_GRAYSCALE)
  bit_stream = read_binary_image(img)
  new_bit_stream = bit_streamRandoming(bit_stream)

  # bit_streamRandoming(bit_stream)
  # zero, one = bit_streamAnalysing(bit_stream)
  # print("0百分比:",zero)
  # print("1百分比:",one)
  # bit_stream, _ = bit_streamNormalizing(bit_stream)
  # zero, one = bit_streamAnalysing(bit_stream)
  # print("0百分比:",zero)
  # print("1百分比:",one)
  # bit_stream = bit_streamRecovering(bit_stream, 1)
  # zero, one = bit_streamAnalysing(bit_stream)
  # print(zero, one)

pass