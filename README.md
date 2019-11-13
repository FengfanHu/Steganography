# Steganography 信息隐藏作业

## OpenCV

### Install
    pip3 install opencv-python
### Usage

读取图像 (灰度图像)返回numpy.uint8
```python3
img = cv2.imread("../src/original.bmp", cv2.IMREAD_GRAYSCALE)
```
读取RGB图像 返回numpy.ndarray
```python3
img = cv2.imread("../original.png", cv2.IMREAD_COLOR)
```
获取 灰度值
```python3
grey_value = img[0,0]
grey_value2 = img.item(0,0)
```
修改 灰度值
```python3
img.itemset((0,0),100)
```
图像 Size
```python3
shape = img.shape
size = img.size
rows = img.shape[0]
columns = img.shape[1]
```
数据类型 Dtype
```python3
img.dtype
```
写入 图像
```python3
cv2.imwrite("../src/output2.bmp", img)
```
显示 图像
```python3
cv2.imshow('img', img)
```
ESC 捕捉事件
```python3
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
```

***

## LSB
Least significant bit plane

### Usage
 - Embed
 
Dec to bit
```python3
def dec2bit(grey_value) str
```
Read file
```python3
def read_file(path) bit_stream
```
LSB process
```python3
def lsb_process(img, bit_stream)
```

 - Extract
 
Extract values from the least significant bit plane
```python3
def extract_lsb(img, length) bit_stream
```
Transform bit-stream to str format
```python3
def bit_stream2str(bit_stream) str
```

***

## DCT
Discrete Cosine Transform

### Usage
 - Embed
 
Resize the image to a format of 8N*8N
```python3
def img_resize(img) img
```
Split the image-array to a list of block(8*8)
```python3
def img_split(img) (blocks, column_count, row_count)
```
Have each block DCT
```python3
def blocks_dct(blocks) dct_blocks
```
Embed the water print to original image
```python3
def embed_img(dct_blocks, water_print) dct_blocks
```
Have each block IDCT
```python3
def blocks_idct(dct_blocks) idct_blocks
```
Merge the blocks to image-array
```python3
def blocks2img(blocks, row_count, column_count) img
```
 - Extract
 
Extract the water print to original image
```python3
def extract_img(e_img, o_img, wp_row, wp_column) img
```
