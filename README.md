### **Acceleration due to Gravity**

This project was done in order to complete a physics lab. It is written in Python 2 and uses OpenCV.

### Rundown:
**physics.py** reads in the video file and finds the center of the ball, outputting the points. Outputs overlay.mov

**physics1.py** uses the outputted values (manually) and keeps only every 15th point. (Uses points every 15th frame)

**physicsDrawPoints.py** then uses those points to draw the displacement and velocity vectors. Outputs vectors.png

**physicsDrawAccel.py** very similarly to physicsDrawPoints.py creates vectors1.png where the acceleration vectors are more pronounced. It then calculates the magnitude of the acceleration due to gravity.
