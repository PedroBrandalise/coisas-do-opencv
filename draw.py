import numpy as np 
import cv2

#criar uma imagem preta
#na matriz temos uma imagem com 512 por 512, e cada nivel de cor eh zero
img = np.zeros( (512,512,3), np.uint8 )

# desenhar uma linha diagonal com grossura 5px
#comeco, final,  cor, grossura
cv2.line(img,(0,0),(511,511), (255,0,0), 5   )

cv2.rectangle(img,(384,0), (510,128), (0,255,0), 3)
#centro , (comprimento do eixo maior ,  do menor, ..
cv2.ellipse(img,(256,256), (100,50),0,0,180,255,-1)

cv2.imshow('',img)
cv2.waitKey(0)

