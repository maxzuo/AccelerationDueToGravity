import numpy
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import cv2
import os
from datetime import datetime

cap = cv2.VideoCapture("./original.m4v") #Change this is just an example

frameNum = 0

points = []
ROI = []

fps = 240.0
capSize = (1080,720) # this is the size of my source video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')# note the lower case
vout = cv2.VideoWriter()
_ = vout.open('res.mov',fourcc,fps,capSize,True) 


dst1 = None

while True:

	boolean, frame = cap.read()

	# print frame.shape[1]	

	if not boolean:
		break
	if type(frame) == type(None):
		continue

	frame1 = frame[0:720, 200:frame.shape[1]]
	color = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

	lower_green = numpy.array([30, 140, 30])
	upper_green = numpy.array([600, 600, 600])

	mask = cv2.inRange(color, lower_green, upper_green)
	res = cv2.bitwise_and(frame1, frame1, mask=mask)

	grayRes = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
	_, thresholdedRes = cv2.threshold(grayRes, 40, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

	corners = cv2.goodFeaturesToTrack(thresholdedRes, 20, 0.1, 10)

	mask_inv = cv2.bitwise_not(thresholdedRes)

	frame_bg = cv2.bitwise_and(frame1, frame1, mask=thresholdedRes)
	img2_fg = cv2.bitwise_and(res, res, mask=mask_inv)

	dst = cv2.add(frame_bg, img2_fg)

	#frame[0:720, 200:frame.shape[1]] = dst


	if type(corners) == type(None):
		corners = []

	if len(corners) != 0:
		corners = numpy.int0(corners)

		xValues = []
		yValues = []

		for corner in corners:
			x, y = corner.ravel()

			xValues.append(x)
			yValues.append(y)

		averageX = int(sum(xValues)/len(xValues))
		averageY = int(sum(yValues)/len(yValues))

		cv2.circle(frame, (averageX + 200, averageY), 12, (100, 100, 255), -1)




	k = cv2.waitKey(1) & 0xFF
	if k ==ord('q'):
		# cv2.imwrite("final.png", frame)
		break

	# cv2.imshow("Hey", res)
	# cv2.imshow("Color", res)
	vout.write(res)
	# cv2.imshow("Hello", dstThreshold)

cap.release()
vout.release()
vout = None

cv2.destroyAllWindows()