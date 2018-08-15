import cv2
import numpy as np

img = cv2.imread('biblioteca.jpg',0 )
rows,col = img.shape

m= np.float32([ [1,0,100],
                [0,1,50]])

dst = cv2.warpAffine(img, m, (col,rows))

print(img)
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()