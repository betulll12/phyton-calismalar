import cv2
# alinan = cv2.VideoCapture("ornekvideo.mp4")
alinan = cv2.VideoCapture(0)
while True:
    _, resim = alinan.read()
    cv2.imshow("Videooo", resim)
    tus = cv2.waitKey(1)
    print(tus)
    if tus == ord("q"): break