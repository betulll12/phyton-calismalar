# gorunti alma
import cv2
r = cv2.imread("resimler/resim1.jpg")
r2 = cv2.imread("resimler/resim2.png",0)


cv2.imshow("resim1",r)
cv2.imshow("resim2",r2)
cv2.waitKey(0)
