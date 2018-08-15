import cv2
import numpy as np 


def nothing(x):
	pass

#criar uma imagem preta, uma janela
color = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

#criar as trackbars 
cv2.createTrackbar('R', 'image',0,255,nothing)
cv2.createTrackbar('G', 'image',0,255,nothing)
cv2.createTrackbar('B', 'image',0,255,nothing)

switch="off/on"
cv2.createTrackbar(switch, 'image', 0,1,nothing)

while 1:
	cv2.imshow('image',color)
	k=cv2.waitKey(1) & 0xFF
	if k == 27:
		break

	r = cv2.getTrackbarPos('R', 'image')
	g = cv2.getTrackbarPos('G', 'image')
	b = cv2.getTrackbarPos('B', 'image')
	s = cv2.getTrackbarPos(switch, 'image')
	if s==0:
		color[:] = 255
	else:
		color[:] = [b,g,r]

