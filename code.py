import numpy as np
import cv2

img = cv2.imread("C:\Users\Jeffry\Pictures\Capture7.png")
height, width, channels = img.shape
cv2.namedWindow('before',cv2.WINDOW_NORMAL)
cv2.resizeWindow('before', 741,496)
cv2.imshow('before',img)
copy = cv2.imread("C:\Users\Jeffry\Pictures\Capture7.png")

# Insialiasai variabel untuk menghitung frekuensi tiap intensitas
blueSum=[0]*256
greenSum=[0]*256
redSum=[0]*256
 
#Menghitung intensitas, c untuk warna(BGR), w=width,h=height
for c in range(0, 3):
    for w in range(0, width):
        for h in range(0, height):
            if c == 0:
                for iteration in range(0,255):
                    if iteration == img.item(h,w,0) :
                        blueSum[iteration] = blueSum[iteration]
            if c == 1:
                for iteration in range(0,255):
                    if iteration == img.item(h,w,1) :
                        greenSum[iteration] = greenSum[iteration]
            if c == 2 :
                for iteration in range(0,255):
                    if iteration == img.item(h,w,2) :
                        redSum[iteration] = redSum[iteration]
 
#Hitung cdf tiap warna
cdfBlue= [0]*255
cdfGreen= [0]*255
cdfRed= [0]*255
for d in range(0,255):
    if d == 0:
        cdfBlue[d]=round((blueSum[d]/(width*height)),4)
cdfGreen[d]=round((greenSum[d]/(width*height)),4)
        cdfRed[d]=round((redSum[d]/(width*height)),4)
    if d>0:
        cdfBlue[d]=round(((blueSum[d]/(width*height))),4) + cdfBlue[d-1]
        cdfGreen[d]=round(((greenSum[d]/(width*height))),4) + cdfGreen[d-1]
        cdfRed[d]=round(((redSum[d]/(width*height))),4) + cdfRed[d-1]
 
#loop untuk mengganti tiap warna
for f in range(0,255):
    for w in range(0, width):
        for h in range(0, height):
            if img.item(h,w,0) == f:
                if img.item(h,w,0)!= 255:
                    copy.itemset((h,w,0), round(((cdfBlue[f]*255)),4))
    for w in range(0, width):
        for h in range(0, height):
            if f == img.item(h,w,1):
                if img.item(h,w,1)!= 255:
                    copy.itemset((h,w,1), round(((cdfGreen[f]*255)),4))
    for w in range(0, width):
        for h in range(0, height):
            if f == img.item(h,w,2):
                if img.item(h,w,2)!= 255:
                    copy.itemset((h,w,2),round(((cdfRed[f]*255)),4))
 
cv2.namedWindow('after',cv2.WINDOW_NORMAL)
cv2.resizeWindow('after', 741,496)
cv2.imshow('after',copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

 
