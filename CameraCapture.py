import cv
import time
from threading import Timer

class VideoCapturer:
    def __init__(self, callback, interval=0):
        self.callback = callback
        self.interval = interval
        self.capture = cv.CreateCameraCapture(0)
        self.width = int(cv.GetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_WIDTH))
        self.height = int(cv.GetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
           
    def startCapturing(self):
        self.timer = Timer(self.interval, self.callback, [self.capture])
        self.timer.start()

    def finishCapturing(self):
        self.timer.cancel()

if __name__ == "__main__":
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
        #time.sleep(1)
        cv.ShowImage("camera", img)
        k = cv.WaitKey(10);
        if k == -1:
            cv.DestroyWindow("camera")
            break
