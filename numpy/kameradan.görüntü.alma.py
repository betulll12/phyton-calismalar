# cameradan görüntü alma
import cv2
# kaynak = cv2.VideoCapture("resimler/file_example_MP4_480_1_5MG.mp4")
kaynak = cv2.VideoCapture(0)


xx = True
while True:
    xx, resim = kaynak.read()
    # print(xx)
    tus = cv2.waitKey(1)
    if tus == 97 or xx==False: break
    cv2.imshow("video1",resim)