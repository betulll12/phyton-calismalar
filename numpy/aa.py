#pipinstall
# import cv2, numpy
# aa = cv2.imread("Adsiz.png")
# print(aa)
# aa[3][3]=[0,0,0]
# aa[3][4]=[255,255,255]
# cv2.imwrite("yeniresim1.png",aa)
# print(aa)
# # aşağıdaki gibi ilk kodlarımızı yazın
# import numpy
# xx = numpy.array([1, 2, 3, 4, 5])
# print(xx)
# # aşağıdaki gibi ilk kodlarınızı yazın
# import numpy
# xx = numpy.array([
#     [0, 150, 0],  # BGR
#     [0, 0, 255],
#     [200, 0, 0],
#     [255, 0, 255]
# ])

# print(xx)

# import cv2
# cv2.imwrite("deneme1.png", xx)
# # aşağıdaki gibi ilk kodlarınızı yazın
# import numpy
# xx = numpy.array([
#     [0, 150, 0],  # BGR
#     [0, 0, 255],
#     [200, 0, 0],
#     [255, 0, 255]
# ])

# print(xx)

# import cv2
# cv2.imwrite("deneme1.png", xx)
# # aşağıdaki gibi ilk kodlarınızı yazın
# import numpy
# xx = numpy.array([
#    [ [0, 150, 0],  # BGR
#     [200, 0, 0],
#     [255, 0, 255]]
# ])

# print(xx)

# import cv2
# cv2.imwrite("deneme2.png", xx)
# import numpy
# xx = numpy.array([
#    #[ [0, 0, 0],[255, 255, 255],[150, 150, 150],]
#  [0, 255, 150],
# ])

# print(xx)

# import cv2
# cv2.imwrite("deneme3.png", xx)

# pip install opencv-python
import cv2, numpy  # pip install opencv-python
aa = cv2.imread("resimler/resim1.jpg")
print(aa)
print("Dizi boyutu:", aa.ndim)
cv2.imwrite("numpydaresim.png", aa)

parca = aa[:20]
cv2.imwrite("parca.png", parca)
parca1 = aa[:, :20]
cv2.imwrite("parca1.png", parca1)

