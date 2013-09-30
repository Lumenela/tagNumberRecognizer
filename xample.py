import cv,numpy   #

#
capture = cv.CaptureFromCAM(0)

image = cv.QueryFrame(capture)

height = image.height
width  = image.width
print height,width


#
gray    = cv.CreateImage(cv.GetSize(image),cv.IPL_DEPTH_8U, 1 )
binary  = cv.CreateImage(cv.GetSize(image),cv.IPL_DEPTH_8U, 1 )
dst1    = cv.CreateImage(cv.GetSize(image),cv.IPL_DEPTH_8U, 1 )

#
cv.CvtColor(image,gray,cv.CV_RGB2GRAY)
#
cv.InRangeS(gray,cv.Scalar(30),cv.Scalar(200),binary)

#
storage = cv.CreateMemStorage(0)
#
contours = cv.FindContours(binary,storage,
cv.CV_RETR_TREE,cv.CV_CHAIN_APPROX_SIMPLE ,(0,0))

#
while contours!= None:
    cv.DrawContours(dst1,contours,cv.CV_RGB(250,0,0), cv.CV_RGB(0,0,250),2,1,8)
    contours = contours.h_next()

#
mat = cv.GetMat(dst1,0)


#
cv.Save('matrix.xml',mat)

#
cv.NamedWindow('original',cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow('gray',cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow('Contours',cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow('Binary',cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('original',image)
cv.ShowImage('gray',gray)
cv.ShowImage('Contours',dst1)
cv.ShowImage('Binary',binary)
cv.WaitKey(0) #