from cv2 import cv2
import visible, ste_embed

if __name__ == "__main__":
  img = cv2.imread('../src/test/1-2.bmp', cv2.IMREAD_GRAYSCALE)
  img = visible.lsb(img, 7)
  cv2.imshow('test', img)
  k = cv2.waitKey(0)
  if k == 27:
    cv2.destroyAllWindows()
  