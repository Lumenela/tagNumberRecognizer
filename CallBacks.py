import cv

class JPEGWriterCallback:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, image):
        cv.SaveImage(self.filename, image)
