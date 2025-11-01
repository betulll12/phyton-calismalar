import numpy as np, cv2
# d1 = np.full((40, 60), 150, np.uint8)
d1 = np.full((40, 60, 3), [0, 250, 0], np.uint8)
print(d1)

cv2.imshow("resim", d1)
cv2.waitKey(0)