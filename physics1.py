import numpy
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import cv2
import os
from datetime import datetime

cap = cv2.VideoCapture("./Samples/movie.m4v") #Change this is just an example

frameNum = 0

points = []

while True:

	boolean, frame = cap.read()

	points = [[225, 714], [225, 714], [226, 708], [230, 702], [228, 695], [238, 690], [239, 680], [243, 669], [244, 660], [250, 648], [251, 634], [252, 624], [256, 612], [255, 602], [262, 590], [267, 582], [266, 572], [266, 572], [270, 559], [274, 546], [272, 537], [278, 528], [280, 519], [282, 509], [288, 496], [288, 489], [291, 482], [296, 467], [296, 463], [302, 453], [302, 446], [307, 439], [309, 425], [309, 425], [311, 417], [310, 408], [316, 404], [319, 396], [320, 388], [320, 378], [322, 371], [326, 362], [331, 355], [330, 346], [336, 339], [341, 332], [338, 325], [344, 318], [346, 315], [346, 315], [351, 307], [350, 300], [352, 295], [357, 288], [357, 283], [363, 276], [363, 267], [367, 263], [369, 258], [371, 253], [375, 248], [374, 243], [377, 238], [380, 231], [383, 228], [383, 228], [387, 223], [387, 216], [392, 213], [394, 207], [398, 204], [401, 202], [400, 197], [402, 191], [407, 189], [411, 182], [410, 178], [415, 175], [417, 173], [417, 171], [421, 169], [421, 169], [426, 164], [430, 159], [435, 156], [435, 154], [439, 156], [438, 151], [447, 150], [444, 146], [446, 144], [453, 141], [453, 139], [457, 137], [453, 135], [459, 137], [462, 131], [462, 131], [464, 132], [471, 130], [472, 128], [471, 125], [476, 125], [478, 124], [482, 123], [483, 122], [483, 121], [486, 121], [494, 122], [494, 124], [499, 122], [500, 121], [503, 123], [503, 123], [503, 121], [507, 123], [512, 120], [512, 125], [516, 123], [520, 124], [521, 124], [522, 125], [527, 129], [528, 127], [528, 130], [536, 135], [536, 131], [541, 134], [544, 136], [544, 136], [545, 139], [547, 140], [552, 143], [554, 144], [554, 146], [560, 149], [564, 154], [563, 154], [567, 156], [568, 161], [572, 164], [573, 165], [579, 170], [581, 175], [586, 177], [586, 177], [584, 183], [590, 185], [594, 188], [596, 192], [601, 193], [602, 203], [604, 202], [609, 208], [613, 214], [611, 215], [616, 225], [620, 227], [621, 231], [625, 234], [628, 245], [628, 245], [631, 246], [634, 254], [637, 260], [638, 264], [640, 269], [647, 277], [648, 285], [649, 289], [655, 296], [657, 299], [658, 310], [664, 316], [665, 324], [671, 330], [672, 338], [672, 338], [677, 344], [678, 349], [682, 361], [685, 363], [687, 375], [689, 378], [693, 386], [696, 396], [701, 409], [704, 415], [708, 425], [707, 431], [714, 439], [716, 453], [716, 459], [716, 459], [721, 470], [724, 473], [729, 486], [731, 496], [735, 505], [737, 515], [745, 525], [745, 537], [744, 550], [753, 562], [753, 568], [759, 579], [763, 593], [767, 605], [766, 611], [766, 611], [770, 628], [776, 637], [779, 647], [784, 662], [785, 673], [785, 685], [790, 693], [790, 698], [797, 705], [801, 716], [203, 718], [224, 718], [224, 717]]

	for point in points:
		frameNum += 1
		if frameNum % 15 != 0:
			continue
		cv2.circle(frame, (point[0] + 200, point[1]), 4, (200, 0, 255), -1)

	cv2.imwrite("test.png", frame)
	break
cap.release()
cv2.destroyAllWindows()