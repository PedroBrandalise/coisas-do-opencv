import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

while(True):
	#capturar frame por frame
	ret, frame = cap.read()

	#operacoes no frame
	gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#mostrar os resultados
	cv2.imshow('frame', gray)
	if cv2.waitKey(0) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()