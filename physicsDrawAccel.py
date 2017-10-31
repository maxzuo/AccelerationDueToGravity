import numpy
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import cv2
import math

img = cv2.imread("test.png")

points = [[262, 590], [302, 453], [336, 339], [371, 253], [407, 189], [444, 146], [482, 123], [520, 124], [554, 146], [596, 192], [637, 260], [678, 349], [721, 470], [766, 611]]
velocities = []

TENCM = 727 - 665
CENTER = (727, 398)

mousePos = [None, None]

def mouseClick(event, x, y, flags, param):
	global mousePos
	print x, y
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img, (x, y), 4, (100, 255, 100), -1)
		mousePos = [x, y]
		print "\n\n" + str(mousePos) + "\n\n"

cv2.namedWindow("image")
# cv2.setMouseCallback('image', mouseClick)

while(1):
	for point in points:
		cv2.arrowedLine(img, CENTER, (point[0] + 200, point[1]), (255, 150, 100), 2, tipLength = 0.05)

	color = 0
	for i in range(0, len(points) - 1):
		cv2.arrowedLine(img, (points[i][0] + 200, points[i][1]), (points[i+1][0] + 200, points[i+1][1]), (150 - color, 255, 100 - color/4), 1, tipLength = 0.05)
		if color == 0:
			color = 120
		else: color = 0
	font = cv2.FONT_HERSHEY_SIMPLEX
	color = 0
	velPoints = []
	for i in range(0, len(points)-1):
		# cv2.arrowedLine(img, (points[i][0] + 200, points[i][1]), (points[i+1][0] + 200, points[i+1][1]), (150, 255, 100), 2, tipLength = 0.05)
		displacement = [points[i+1][0] - points[i][0], points[i + 1][1] - points[i][1]]

		magnitude = (math.sqrt(float(displacement[0] **2 + displacement[1] ** 2)))
		converted = magnitude/float(TENCM) * 10.0/100.0
		converted = math.floor(converted * 10000 + 0.5)/10000
		# print str(converted) + " cm"
		averagePoint = [int((points[i][0] + points[i+1][0])/2) + 200, int((points[i][1] + points[i+1][1])/2)]

		velocities.append(displacement)

		velPoint = [(points[i+1][0] + 200 + displacement[0]), (points[i+1][1] + displacement[1])]
		velPoints.append(velPoint)
		
		
		stringConverted = str(converted) + " m"
		if stringConverted == "0.158 m": stringConverted = "0.1580 m"
		# cv2.putText(img, stringConverted, (averagePoint[0], averagePoint[1]), font, 0.45, (10, 10, 245), 1, cv2.LINE_AA)


		cv2.arrowedLine(img, (points[i+1][0] + 200, points[i+1][1]), (velPoint[0], velPoint[1]), (100, 150 - color, 255), 1, tipLength = 0.08)

		if color == 0:
			color = 100
		else: color = 0
	accel = []
	for i in range(0, len(velPoints) - 2):
		velocity = velocities[i]
		velPoint = velPoints[i]
		velPoint1 = [points[i+2][0] + 200, points[i+2][1]]

		averagePoint = [int((velPoint[0] + velPoint1[0])/2), int((velPoint[1] + velPoint1[1])/2)]
		# print (math.sqrt(float(velPoint[0] - velPoint1[0]) **2 + float((velPoint[1] - velPoint1[1]) ** 2)))
		# print magnitude/float(TENCM) * 10.0/100.0

		magnitude = (math.sqrt(float(velPoint[0] - velPoint1[0]) **2 + float((velPoint[1] - velPoint1[1]) ** 2)))
		converted = magnitude/float(TENCM) * 10.0/100.0
		converted = math.floor(converted * 10000 + 0.5)/10000

		accel.append(converted)

		cv2.putText(img, str(converted), (averagePoint[0], averagePoint[1]), font, 0.30, (10, 10, 245), 1, cv2.LINE_AA)
		cv2.arrowedLine(img, (velPoint[0], velPoint[1]), (velPoint1[0], velPoint1[1]), (100, 150 - color, 255), 3, tipLength = 0.1)


	print img.shape
	text = "Average acceleration calculated by computer to be: -" + str(math.floor((sum(accel)/len(accel))/((15.0/240.0)**2) * 1000.0)/1000.0) + " m/s^2"
	print text
	cv2.putText(img, text, (30, img.shape[0] - 50), font, 1, (60, 10, 255), 1, cv2.LINE_AA)

	# for i in range(0, len(velocities) - 1)

	# cv2.imshow("image", img)
	cv2.imwrite("vectors1.png", img)
	break
	k = cv2.waitKey(1) & 0xFF
	if k == ord('q'):
		break

cv2.destroyAllWindows()

"""

Origin: 727 398

left: 665 320
right: 721 371

721 - 665 = 

"""