import cv

class JPEGWriterCallback:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, img):
        cv.SaveImage(self.filename, img)

class JPEGSeriesWriterCallback:
    def __init__(self, fileprefix):
        self.counter = 0
        self.fileprefix = fileprefix
    
    def __call__(self, img):
        cv.SaveImage(self.fileprefix + "%03d" % (self.counter) + ".jpg", img)
        self.counter += 1