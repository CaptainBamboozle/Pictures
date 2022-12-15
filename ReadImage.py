from email.mime import image
from tkinter import Image
import cv2
image=cv2.imread("C:/Users/farid/Downloads/fat luffy.jpg")
cv2.imshow("Fat Luffy Revealed",image)
#cv2.waitKey(0)
#print(image)

grayimage=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow("Fat Luffy 1800s",grayimage)
print(grayimage)
cv2.waitKey(0)