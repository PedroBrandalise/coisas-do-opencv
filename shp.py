import cv2
import numpy as np 
from matplotlib import pyplot as plt
#importar a imagem
img=cv2.imread('foto.jpeg')
#criar a mascara
kernel =np.array  ([[ 0.,-1., 0.],
					[-1., 4.,-1.],
				  	[ 0.,-1., 0.]])
print(kernel) #mostra a mascara usada no terminal
dst = cv2.filter2D(img, -1, kernel)

#plotar imagem
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Aplicado')
plt.xticks([]), plt.yticks([])
plt.show()