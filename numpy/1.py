import numpy as np
d1 = np.full((40, 60), 150, np.uint8)
print(d1)

import cv2
cv2.imshow("resim", d1)
cv2.waitKey(0)