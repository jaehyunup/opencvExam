import cv2
import numpy as np
# setup video capture
cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

while True:
	ret,img = cam.read()
	cv2.imshow("",img)
	if cv2.waitKey(1)==27: # esc
		cv2.imwrite('cameracapture.jpg', img)
cam.realease()

