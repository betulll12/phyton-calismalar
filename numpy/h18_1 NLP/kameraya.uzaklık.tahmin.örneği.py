# KAMERAYA uzaklık tahmin örneği.
import cv2
import numpy as np
from sklearn.svm import SVC  # Basit bir SVM modeli
from sklearn.preprocessing import StandardScaler


# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


# 2. Örnek eğitim verisi (Gerçek modelde buraya eğitim süreci eklenebilir)
X_train = np.array([[100,100],[200, 200],[300,300]])  # Örnek yüz boyutları
y_train = np.array([0, 1, 2])  # Örnek etiketler (0: Normal, 1: Yakın gibi)


model_nesnesi = StandardScaler()
X_train = model_nesnesi.fit_transform(X_train)


model = SVC(kernel="linear")  # Basit bir SVM modeli
model.fit(X_train, y_train)


# 1. OpenCV ile Kamerayı Aç
kameraG = cv2.VideoCapture(0)  # 0, varsayılan kamerayı kullanır
while True:
    ret, resim = kameraG.read()
   
    gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
    yuzler = face_cascade.detectMultiScale(gri_resim, scaleFactor=1.3, minNeighbors=5)


    for (x, y, w, h) in yuzler:
        # 3. Yüzü Çerçeve İçinde Göster
        cv2.rectangle(resim, (x, y), (x + w, y + h), (255, 0, 255), 2)


        # 4. Yüzü Makine Öğrenmesi Modeline Gönder
        yuz_ozellik = np.array([[w, h]])  # Basit olarak yüz genişliği ve yüksekliği
        yuz_ozellik = model_nesnesi.transform(yuz_ozellik)
        tahmin_sinifi = model.predict(yuz_ozellik)


        # label = f"Cok yakinsin w:{w}, h:{h}" if tahmin_sinifi[0] == 0 else f"Cok yakinsin w:{w}, h:{h}"
        if tahmin_sinifi[0] == 0: label = f"Cok uzaksin w:{w}, h:{h}"
        if tahmin_sinifi[0] == 1: label = f"Normal w:{w}, h:{h}"
        if tahmin_sinifi[0] == 2: label = f"Cok yakinsin w:{w}, h:{h}"
        cv2.putText(resim, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)


    cv2.imshow("Kamera Görüntüsü", resim)


    if cv2.waitKey(1) & 0xFF == ord("q"):  # 'q' ile çıkış
        break


kameraG.release()
cv2.destroyAllWindows()




