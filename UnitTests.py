import unittest
import time
from CameraCapture import VideoCapturer
from CallBacks import JPEGWriterCallback
from CallBacks import JPEGSeriesWriterCallback

class VideoCapturerAndCallBacksTestCase(unittest.TestCase):
    def setUp(self):
        self.testfilename = "testfilename.jpg"
        self.capturer = VideoCapturer(JPEGWriterCallback(self.testfilename))

    def testA(self):
        self.capturer.startCapturing()
        time.sleep(1)
        try:
            with open(self.testfilename): pass
        except IOError:
            assert False, "File doesn't exist!"

    def tearDown(self):
        self.capturer.finishCapturing()

class SeriesCallbackTest(unittest.TestCase):
    def setUp(self):
        self.testfileprefix = "testfileprefix"
        self.capturer = VideoCapturer(JPEGSeriesWriterCallback(self.testfileprefix), interval=1)
    
    def test(self):
        self.capturer.startCapturing()
        time.sleep(5)
        try:
            with open(self.testfileprefix + "000" + ".jpg"): pass
            with open(self.testfileprefix + "001" + ".jpg"): pass
            with open(self.testfileprefix + "002" + ".jpg"): pass
        except IOError:
            assert False, "File series doesn't exists!"

    def tearDown(self):
        self.capturer.finishCapturing()

if __name__ == "__main__":
    unittest.main()