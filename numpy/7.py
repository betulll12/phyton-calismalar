import cv2, numpy as np
alinan1 = cv2.VideoCapture(0)
resim2 = cv2.imread("640x480goruntu.png")
while True:
    _, resim1 = alinan1.read()
    cv2.imshow("Videooo1", resim1)
    cv2.imshow("Videooo2", resim2)
    yenid1 = np.hsplit(resim1, 2)
    yenid2 = np.hsplit(resim2, 2)
    # print("resim1.shape : ", resim1.shape)
    # print("resim2.shape : ", resim2.shape)

    # cv2.imshow("Videooo3", resim1[:200])
    # cv2.imshow("Videooo4", resim2[:200])
    # birlesik = np.concatenate((resim1[:200], resim2[:200]))

    birlesik = np.concatenate((yenid1[0], yenid2[0]), axis=1)
    cv2.imshow("Videooo5", birlesik)

    tus = cv2.waitKey(1)
    if tus == ord("q"): break