#borra imagem com o OpenCV
#para isso sera aplicado um FPB

import cv2
import numpy as np 
from matplotlib import pyplot as plt
#importar a imagem
img=cv2.imread('biblioteca.jpg')

#criar a mascara
kernel = np.ones((5,5), np.float32)/25

dst = cv2.filter2D(img, -1, kernel)

#plotar imagem

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Aplicado')
plt.xticks([]), plt.yticks([])
plt.show()
