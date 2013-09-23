import cv
import time


class VideoCapturer:
    def __init__(self, callback):
        self.callback = callback
    
    def startCapturing(self):
        pass

cv.NamedWindow("camera", 1)
capture = cv.CreateCameraCapture(0)

width = None #leave None for auto-detection
height = None #leave None for auto-detection

if width is None:
    width = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH))
else:
	cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_WIDTH,width)    

if height is None:
	height = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
else:
	cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_HEIGHT,height) 

while True:
    img = cv.QueryFrame(capture)
    print type(img)
    print dir(img)
    cv.ShowImage("camera", img)
    cv.SaveImage("temp.jpg", img)
    k = cv.WaitKey(10);
    if k == 'f':
        break
