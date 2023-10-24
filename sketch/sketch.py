# library numpy -> pip install numpy
# library imageio -> pip install imageio
# library scipy -> pip install scipy
# library opencv -> pip install opencv-python 
# kita pakai library image yang kemarin (pip install image)
# siapkan 1 gambar di folder yang sama untuk diconvert menjadi sketsa pensil

# import library yang akan digunakan
import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "jester.jpg" #nama file input
 
def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])
#formula untuk convert img -> grayscale//pakai kode warna matlab

def dodge(front,back):
    final_sketch = front*225/(225-back)
    #kalau gambarnya lebih besar dari 225 bit/px maka akan discovert jadi 225
    final_sketch[final_sketch>225]=225
    final_sketch[back==225]=225

    return final_sketch.astype('uint8')

#untuk read gambar yang di pilih diawal tadi
ss = imageio.imread(img) #untuk read gambar yang dipilih diawal tadi
gray = rgb2gray(ss)#untuk discovert gambar jadi black dan white

i = 255-gray

#untuk memberi efek blur
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)
#sigma=15  adalah intensias blurnya

r = dodge(blur,gray)
#untuk convert gambarnya (dengan mengaplikasikan blur & BlackWhite tadi)

cv2.imwrite("sketsa.png", r)
#untuk menghasilkan output gambar bernama sketsa.png
# run > start debugging
