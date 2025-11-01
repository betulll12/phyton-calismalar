 #split (dizi/resim bölme)
import numpy as np, cv2
# arr = np.array([7,2,3,4,5,6,8])
arr = cv2.imread("resimler/resim2.png")
newarr = np.array_split(arr, 3)

cv2.imshow("parca1",newarr[2])
cv2.waitKey(0) 
cv2.imshow("parca1",newarr[2])
#ile alınan parça 
