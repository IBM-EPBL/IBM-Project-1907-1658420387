# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 18:33:34 2022

@author: DELL
"""

import cv2

video = cv2.VideoCapture(0)

while True:
	ret, frame = video.read()
	cv2.imshow("Frame", frame)
	k = cv2.waitKey(1)
	if k == ord('q'):
		break

video.release()
cv2.destroyAllWindows()