import numpy as np, cv2
d1 = np.full((40, 260, 3), [0, 200, 200], np.uint8)
d2 = np.full((40, 260, 3), [0, 0, 250], np.uint8)

cv2.imshow("resim1", d1) # "resim1" pencere başlığı,# d1 gösterilecek resim
cv2.imshow("resim2", d2) # imshow metotlarındaki pencere başlığı farklı olmalı
d3 = np.concatenate((d2, d1))
cv2.imshow("resim3", d3)

cv2.waitKey(0) #bir tuşa basılıncaya kadar pencereler ekranda kalır.
