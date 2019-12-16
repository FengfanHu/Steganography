#Take least significant bit plane
from cv2 import cv2
import ste_embed

#From gray image extract binary water mark.
def lsb(img, depth):
  rows = img.shape[0]
  columns = img.shape[1]
  for row in range(rows):
    for column in range(columns):
      value = img.item(row, column)
      value_str = ste_embed.dec2bit(value)
      temp = int(value_str[depth-1])
      if temp:
        temp = 255
      img.itemset((row,column), temp)
  return img

#From RGB image extract binary water mark.
def lsb_rgb(img, c_type, depth):
  rows = img.shape[0]
  columns = img.shape[1]
  for row in range(rows):
    for column in range(columns):
      value = img.item(row, column, c_type)
      value_str = ste_embed.dec2bit(value)
      temp = int(value_str[depth-1])
      if temp:
        temp = 255
      img.itemset((row,column, c_type), temp)
  return img

if __name__ == "__main__":
  original_img = cv2.imread('../src/test/50-2.bmp', cv2.IMREAD_COLOR)
  img_r = original_img[:,:,0]
  img_g = original_img[:,:,1]
  img_b = original_img[:,:,2]
  # embedded_img = cv2.imread('../src/lsb/embedded.bmp', cv2.IMREAD_GRAYSCALE)
  r_lsb = lsb_rgb(original_img, 0, 8)
  g_lsb = lsb_rgb(original_img, 1, 8)
  b_lsb = lsb_rgb(original_img, 2, 8)
  # embedded_lsb = lsb(embedded_img)
  cv2.imshow('R', r_lsb)
  cv2.imshow('G', g_lsb)
  cv2.imshow('B', b_lsb)
  # cv2.imshow('embedded_lsb', embedded_lsb)
  k = cv2.waitKey(0)
  if k == 27:
    cv2.destroyAllWindows()
