import unittest
from CameraCapture import VideoCapturer
from CallBacks import JPEGWriterCallback

class VideoCapturerAndCallBacksTestCase(unittest.TestCase):
    def setUp(self):
        self.capturer = VideoCapturer(JPEGWriterCallback())

    def testA(self):
        self.capturer.startCapturing()
        assert True, "Won't be written"
    
    def tearDown(self):
        self.capturer.finishCapturing()

if __name__ == "__main__":
    unittest.main()