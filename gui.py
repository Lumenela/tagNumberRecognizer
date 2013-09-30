import cv
import cv2
import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QImage
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from CameraCapture import VideoCapturer
import CallBacks

from guiInit import Ui_MainWindow
 
import time, threading

class VideoTimer:
    def __init__(self, frame):
        self.frame = frame

    def __call__(self):
        self.frame.reloadImage()
        threading.Timer(0.03, self).start()


class Frame(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.capturer = VideoCapturer(self)

        width = int(cv.GetCaptureProperty(self.capturer.capture, cv.CV_CAP_PROP_FRAME_WIDTH))
        height = int(cv.GetCaptureProperty(self.capturer.capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
        self.resize(width, height)

        self.reloadImage()

        video = VideoTimer(self)
        video()

    def reloadImage(self):
		
        img = cv.QueryFrame(self.capturer.capture)

        palette = QPalette()
        qimage = QImage(img.tostring(), img.width, img.height, QImage.Format_RGB888).rgbSwapped()
        #qimage = cv2.cvtColor( qimage, cv2.COLOR_RGB2GRAY )
        palette.setBrush(QPalette.Background,QBrush(qimage))
        
        self.setPalette(palette)
            
    def mousePressEvent(self, event):
        self.reloadImage()
                
    def __call__(self, img):
        image = QImage(img.tostring(), img.width, img.height, QImage.Format_RGB888)
            
    def closeEvent(self, event):
        self.capturer.finishCapturing()


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)

    frame = Frame()
    frame.show()
    
    sys.exit(app.exec_())
