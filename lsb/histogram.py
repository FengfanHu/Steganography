from  cv2 import cv2
from matplotlib import pyplot as plt

def count_value(path):
  img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
  rows = img.shape[0]
  columns = img.shape[1]
  pixel_value = []
  gary_index = []
  for i in range(256):
      pixel_value.append(0)
      gary_index.append(i)
  #Count each value (from 0 to 255)
  for row in range(rows):
    for column in range(columns):
      pixel_value[img.item(row, column)] = pixel_value[img.item(row, column)] + 1
  return gary_index, pixel_value

def show_histogram(original_index, original_value, oringal_title, embedded_index, embedded_value, embedded_title):
  plt.rcParams['font.sans-serif'] = 'SimHei'
  plt.rcParams['axes.unicode_minus'] = False
  p1 = plt.figure(figsize=(20, 30))
  ax1 = p1.add_subplot(2, 1, 1)
  plt.bar(original_index, original_value)
  plt.title(oringal_title)
  ax2 = p1.add_subplot(2, 1, 2)
  plt.bar(embedded_index, embedded_value)
  plt.title(embedded_title)
  plt.show()

if __name__ == "__main__":
  original_index, original_value = count_value('../src/lsb/lena.bmp')
  embedded_index, embedded_value = count_value('../src/lsb/embedded.bmp')

  show_histogram(original_index, original_value, "original",
  embedded_index, embedded_value, "embedded")

