# goruntu çevirme
import cv2, numpy
# kaynak = cv2.VideoCapture("resimler/file_example_MP4_480_1_5MG.mp4")
kaynak = cv2.VideoCapture(0)


xx = True
while True:
    xx, resim = kaynak.read()
    # print(xx)
    print(resim.shape)
    tus = cv2.waitKey(1)
    if tus == 97 or xx==False: break
    cv2.imshow("video1",resim)
    kucukresim = cv2.pyrDown(resim)
    print(kucukresim.shape)
    cv2.imshow("video2",kucukresim)
    sbresim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
    cv2.imshow("video3",sbresim)
    cv2.imshow("video4",numpy.transpose(sbresim))