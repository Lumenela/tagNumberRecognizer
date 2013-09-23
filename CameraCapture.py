import cv
import time
from threading import Timer
from threading import Thread
from threading import Event

class RepeatedTimer(Thread):
    def __init__(self, event, callback, interval):
        Thread.__init__(self)
        self.stopped = event
        self.interval = interval
        self.callback = callback

    def run(self):
        while not self.stopped.wait(self.interval):
            self.callback()

class CallbackWrapper:
    def __init__(self, callback, capture):
        self.callback = callback
        self.capture = capture

    def __call__(self):
        self.callback(cv.QueryFrame(self.capture))

class VideoCapturer:
    def __init__(self, callback, interval=0):
        self.callback = callback
        self.interval = interval
        self.capture = cv.CreateCameraCapture(0)
        self.width = int(cv.GetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_WIDTH))
        self.height = int(cv.GetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
           
    def startCapturing(self):
        self.stopped = Event()
        self.timer = RepeatedTimer(self.stopped, CallbackWrapper(self.callback, self.capture), self.interval)
        self.timer.start()

    def finishCapturing(self):
        self.stopped.set()

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
