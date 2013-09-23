import cv

class JPEGWriterCallback:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, capture):
        cv.SaveImage(self.filename, cv.QueryFrame(capture))
