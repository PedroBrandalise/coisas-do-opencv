import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

#define o codec e cria um objeto VideoWriter
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
i=0
while (cap.isOpened()):
	i=i+1
	ret, frame = cap.read()

	if ret == True:
		#frame = cv2.flip(frame,0)

		#escrever o frame flipado
		out.write(frame)

		#cv2.imshow('frame',frame)
		if i==20:
			break
		if cv2.waitKey(1) & 0xFF ==  ord('q'):
			break
	else:
		break

cap.release()
out.release()
cv2.destroyAllWindows()