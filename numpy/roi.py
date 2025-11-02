# roi
import cv2
kaynak = cv2.VideoCapture(0)


xx = True
while True:
    xx, resim = kaynak.read()
    print(xx, resim.shape)
    tus = cv2.waitKey(1)


    if tus == 97 or xx==False: break
    cv2.imshow("video1",cv2.pyrDown(resim))
    cv2.imshow("video2",resim[100:300,100:300])
    resim[0:100,0:100]  = resim[200:300,200:300]
    cv2.imshow("video3",resim)