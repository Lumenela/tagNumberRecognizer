import cv2.cv as cv
import cv2 as cv2
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--Camera', action='store_true', default=False)
parser.add_argument('--Gray', action='store_true', default=False)
parser.add_argument('--Binary', action='store_true', default=False)
parser.add_argument('--Sobel', action='store_true', default=False)
parser.add_argument('--Blur', action='store_true', default=False)
parser.add_argument('--Diff', action='store_true', default=False)
parser.add_argument('--Contours', action='store_true', default=False)

args = parser.parse_args()

if not(args.Camera or args.Gray or args.Binary or args.Sobel or args.Blur or args.Diff):
    args.Contours = True
    
#debug settings
Camera = args.Camera
Gray = args.Gray
Binary = args.Binary
Sobel = args.Sobel
Blur = args.Blur
Diff = args.Diff
Contours = args.Contours

if Camera:
    cv.NamedWindow("Camera", 1)
if Gray:    
    cv.NamedWindow("Gray", 1)
if Binary:    
    cv.NamedWindow("Binary", 1)
if Sobel:
    cv.NamedWindow("Sobel", 1)
if Blur:
    cv.NamedWindow("Blur", 1)
if Diff:
    cv.NamedWindow("Diff", 1)
if Contours:
    cv.NamedWindow("Contours", 1)
    
capture = cv.CaptureFromCAM(0)

while True:

    #create some images
    img = cv.QueryFrame(capture)
    if Camera:
        cv.ShowImage('Camera', img)
    
    #gray
    imgGray  = cv.CreateImage(cv.GetSize(img),cv.IPL_DEPTH_8U,1)
    cv.CvtColor(img,imgGray,cv.CV_RGB2GRAY) #convert to gray
    if Gray:
        cv.ShowImage('Gray', imgGray)
    
    #binary
    imgBinary = cv.CreateImage(cv.GetSize(img),cv.IPL_DEPTH_8U, 1 )
    cv.InRangeS(imgGray,cv.Scalar(30),cv.Scalar(200),imgBinary)
    if Binary:
        cv.ShowImage('Binary', imgBinary)
        
    
    #sobel
    imgSobel = cv.CreateMat(imgGray.height, imgGray.width, cv.CV_32FC1) 
    cv.Sobel(imgGray,imgSobel,1,1,3)
    if Sobel:
        cv.ShowImage('Sobel', imgSobel)
    
    #blur
    imgBlur = cv.CreateImage(cv.GetSize(imgGray), imgGray.depth, imgGray.nChannels)
    cv.Smooth(imgGray, imgBlur, cv.CV_BLUR, 11, 11)
    if Blur:
        cv.ShowImage('Blur', imgBlur)
    
    #diff
    imgDiff = cv.CreateImage(cv.GetSize(imgGray), imgGray.depth, imgGray.nChannels)
    cv.AbsDiff(imgGray,imgBlur,imgDiff)
    if Diff:
        cv.ShowImage('Diff', imgDiff)
        
    #okay, lest maybe find something

    contourStorage = cv.CreateMemStorage(0)    
    contours = cv.FindContours(imgGray,contourStorage,
        cv.CV_RETR_TREE,cv.CV_CHAIN_APPROX_SIMPLE ,(0,0))
    
    #AFNOTE: all this is bat shit :( 
    #imWrite(
    #imgConGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #imgConBlur = cv2.GaussianBlur(gray,(1,1),1000)
    #flag, thresh = cv2.threshold(imgConBlur, 120, 255, cv2.THRESH_BINARY)
    #contours2, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    

    imgContours = cv.CreateImage(cv.GetSize(img),cv.IPL_DEPTH_8U, 1 )

    while contours!= None:
        cv.DrawContours(imgContours,contours,cv.CV_RGB(250,0,0), cv.CV_RGB(0,0,250),2,1,8)
        contours = contours.h_next()    
    
    if Contours:
        cv.ShowImage('Contours', imgContours)
    
    
    
    if cv.WaitKey(10) == 27:
        break
cv.DestroyWindow("Camera")
