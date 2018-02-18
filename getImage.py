# needed to capture image
import cv2
# Import the base64 encoding library to encode image
import base64
 
def capture():
	#Camera 0 = webcam for laptop, this should be changed for USB camera
	camera_port = 0
	 
	camera = cv2.VideoCapture(camera_port)#creates camera object using webcam index
	 
	def get_image():#gets single image
	 retval, im = camera.read()
	 return im
	
	ramp_frames = 30 #takes 30 frames for image calibration
	for i in range(ramp_frames):
		temp = get_image()
	
	camera_capture = get_image()
	file = "./snapShot.png" #file path for the given snapShot
	
	cv2.imwrite(file, camera_capture)
	
	del(camera)#deletes camera in order to create another later