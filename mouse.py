import cv2
import numpy as np

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
color=(0,0,0)
#funcao de retorno de chamada do mouse
def draw_circle2(event,x,y,flags,param):
	global ix,iy,drawing,mode, color

	if event== cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix,iy=x,y;
	elif (event== cv2.EVENT_MOUSEMOVE ):
		if drawing==True:
			cv2.circle(img,(x,y), 10, color, -1)
    	
	elif event==cv2.EVENT_LBUTTONUP:
		drawing=False

img =np.ones( (512,512,3), np.uint8 )*255



cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle2)

cont=0

while (1):
	cv2.imshow('image', img)
	k=cv2.waitKey(1) & 0xFF
	if k==27:
		break
	elif k== ord('s'):
		cv2.imwrite('desenho'+repr(cont)+'.png',img)
		cont=cont+1

cv2.destroyAllWindows()
