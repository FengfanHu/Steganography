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
 
Dec to bit 十进制转二进制
```python3
def dec2bit(grey_value) str
```
Read file 读取文本文字
```python3
def read_file(path) bit_stream
```
read_gray_img 读取灰度图像 
```python3
def read_gray_img(img) bit_stream
```
read_binary_image 读取二值图像
```python3
def read_binary_image(img) bit_stream
```
zero_oneAssembling 生成零一索引列表
```python3
def zero_oneAssembling(bit_stream) (zero_list, one_list)
```
bit_streamAnalysing 分析bit-stream零一比例
```python3
def bit_streamAnalysing(bit_stream) (zero_p, one_p)
```
bit_streamNormalizing 使bit-stream零一分布均匀，并记录改变值的索引
```python3
def bit_streamNormalizing(bit_stream) (bit_stream, flag)
```
bit_streamRandoming 随机打乱bit-stream，并记录索引
```python3
def bit_streamRandoming(bit_stream) new_bit_stream
```
LSB process LSB嵌入操作
```python3
def lsb_process(img, bit_stream)
```

 - Extract
 
random_recover bit_streamRandoming的逆操作
```python3
def random_recover(bit_stream) new_bit_stream
```
bit_streamRecovering bit_streamNormalizing的逆操作
```python3
def bit_streamRecovering(bit_stream) new_bit_stream
```
extract_lsb 提取bit-stream
```python3
def extract_lsb(img, length) bit_stream
```
Transform bit-stream to str format
```python3
def bit_stream2str(bit_stream) str
```
Transform bit-stream to img
```python3
def bit_stream2gray_img(bit_stream, rows, column) img
def bit_stream2binary_img(bit_stream, rows, column) img
```

 - Attack
可视攻击
```python3
def lsb(img, depth) img
def lsb_rgb(img, c_type, depth) img
```
直方图攻击
```python3
def count_value(path) (gary_index, pixel_value)
def show_histogram(original_index, original_value, oringal_title, embedded_index, embedded_value, embedded_title)
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
