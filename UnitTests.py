import unittest
import time
from CameraCapture import VideoCapturer
from CallBacks import JPEGWriterCallback

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
            assert False, "File doesn't exists!"

    def tearDown(self):
        self.capturer.finishCapturing()

if __name__ == "__main__":
    unittest.main()