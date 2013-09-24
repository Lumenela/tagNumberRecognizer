import cv
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

        width = int(cv.GetCaptureProperty(self.capturer.getCapture(), cv.CV_CAP_PROP_FRAME_WIDTH))
        height = int(cv.GetCaptureProperty(self.capturer.getCapture(), cv.CV_CAP_PROP_FRAME_HEIGHT))
        self.resize(width, height)

        self.reloadImage()
        decorator = Ui_MainWindow()
        decorator.setupUi(self)
        self.decorator = decorator
        self.decorator.imageLabel = QtGui.QLabel()

        #video = VideoTimer(self)
        #video()

    def reloadImage(self):
        img = cv.QueryFrame(self.capturer.getCapture())

        palette = QPalette()
        self.centralWidget()
        qimage = QImage(img.tostring(), img.width, img.height, QImage.Format_RGB888).rgbSwapped()
        palette.setBrush(QPalette.Background,QBrush(qimage))
        
        #self.decorator.centralwidget.setPalette(palette)
        
        self.decorator.widget.setPixmap(QtGui.QPixmap.fromImage(qimage))
        self.decorator.scaleFactor = 1.0

        #self.centralWidget().widget.setPalette(palette)

        #self.setWindowIcon(QIcon(qimage))
            
    def mousePressEvent(self, event):
        print "zzz"
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
