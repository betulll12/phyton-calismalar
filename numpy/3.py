import numpy as np, cv2
d1 = np.full((40, 160, 3), [200, 200, 0], np.uint8)
d2 = np.full((40, 160, 3), [0, 0, 250], np.uint8)
# print(d1)

cv2.imshow("resim1", d1) # "resim1" pencere başlığı, d1 gösterilecek resim
cv2.imshow("resim2", d2) # imshow metotlarındaki pencere başlığı farklı olmalı
cv2.waitKey(0)