# karıştırma
import cv2, numpy as np
kaynak = cv2.VideoCapture(0)
kaynak2 = cv2.VideoCapture(1)


while True:
    _ , goruntu = kaynak.read()
    _ , goruntu2 = kaynak2.read()
    sutun, satir = goruntu.shape[:2]


    cv2.imshow("Orjinal Goruntu", cv2.pyrDown(goruntu))
    cv2.imshow("Orjinal Goruntu2", cv2.pyrDown(goruntu2))


    cv2.imshow("Karışmış sekli3", cv2.add(goruntu,goruntu2))
    cv2.imshow("Karışmış sekli4", cv2.addWeighted(goruntu,.3,goruntu2,.7,100))
   
    tus = cv2.waitKey(1)
    if tus == 97: break


