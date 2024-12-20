# -*- coding: utf-8 -*-
"""GoruntuIslemeHafta3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w85so_bSjIu0_B68TYbqTPD4qwRz5L1d

# Kütüphaneler
"""

from google.colab import files
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

"""# Matrisler"""

# Dizilerle işlemler
A = np.array([[1,2,3],[3,4,5]])
A

# Dizilerle işlemler
array1 =np.zeros((2,3))
print(array1)

# Dizilerle işlemler
array2 =np.ones((1,5))
print(array2)

# Dizilerle işlemler
array3 =np.random.rand(5,5)
print(array3)

# 255x255 boyutunda 0 sayısından oluşan bir matris
row=256
col=256
img2=np.zeros((row,col))
print("0 Matrisi:")
print(img2)

# 5x5 boyutunda rastgele sayılardan oluşan bir matris
random_matrix = np.random.rand(5, 5)
print("Rastgele Matris:")
print(random_matrix)

# 10x10 boyutunda rastgele sayılardan oluşan bir matris (görüntü)
image_matrix = np.random.randint(0, 256, (10, 10))  # 0-255 arasında rastgele değerler

# Matrisi görüntü olarak gösterme (gri tonlamalı)
plt.imshow(image_matrix, cmap='gray')
plt.colorbar()  # Renk skalasını gösterme
plt.show()

# 10x10 boyutunda rastgele sayılardan oluşan bir RGB renkli görüntü
rgb_image = np.random.randint(0, 256, (10, 10, 3))  # 3 kanal: Kırmızı, Yeşil, Mavi (RGB)

# Renkli görüntüyü gösterme
plt.imshow(rgb_image)
plt.colorbar()  # Renk skalasını gösterme
plt.show()

# ikili görüntü
height=512
width=512
img3=np.random.randint(255,size=(height,width,1), dtype=np.uint8)
plt.imshow(img3)
plt.colorbar()  # Renk skalasını gösterme
plt.show()

"""# Resimlerle İlk işlemler"""

# Dosya yükleme
uploaded = files.upload()

# Yüklenen dosyayı/resmi açma
for file_name in uploaded.keys():
    img = Image.open("brain1.jpg")

# Resmi görüntüleme
plt.imshow(img)
plt.axis('on')  # Eksenleri aç/kapat
plt.show()

# Resmin boyutlarını (width, height) öğrenme
width, height = img.size
print(f"Resmin boyutu: {width} x {height}")

# Resmin formatı öğrenme
img_type = img.format
print(f"Resmin formatı: {img_type}")

# Resmi NumPy array'e dönüştürme
img_array = np.array(img)

# Resmin veri tipini öğrenme
data_type = img_array.dtype
print(f"Resmin veri tipi: {data_type}")

# Resmin kanal sayısını öğrenme
img.mode
if img.mode == "L": # gri tonlamalı mod
        channels = 1
elif img.mode == "RGB": # RGB mod
        channels = 3
elif img.mode == "RGBA": # RGBA mod
        channels = 4
else:
        channels = "Bilinmeyen"

print(f"Resmin kanal sayısı: {channels}")
print(f"Resmin modu: {img.mode}")

