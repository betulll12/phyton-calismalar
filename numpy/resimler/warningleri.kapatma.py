# Warningleri kapatma
import tensorflow as tf, matplotlib.pyplot as plt, numpy as np
# tensorflow çok fazla warning veriyorsa bunları devre dışı bırakmak için
import warnings;
warnings.filterwarnings("ignore")
# tüm uyarı kategorilerini (DeprecationWarning, FutureWarning, UserWarning vb.) tamamen devre dışı bırakır.


# yukarıdaki satır bazı gerekli warningleri de kapatabileceği için bunun yerine aşağıdakiler daha iyi olabilir.
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)


# 28x28 piksellik El yazısı rakamlar içeren MNIST veri setini yükle
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()# Bir veriyi görselleştirme
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()# Bir veriyi görselleştirme
# fashion_mnist.load_data()
num_labels = len(np.unique(y_train)) # Veri setinde kaç farklı etiket (rakam) olduğunu belirle
print("Farklı etiket sayısı:", num_labels)  # Çıkış: 10 (0'dan 9'a kadar rakamlar)


# Örnek bir görseli ekrana çizdir
plt.figure(figsize=(5, 5))  # Grafik boyutunu ayarla
plt.imshow(x_train[2], cmap='gray')  # 3. resmi gri tonlamada göster
plt.title(f"Etiket: {y_train[2]}")  # Resme ait etiketi başlık olarak ekle
# plt.axis('off')  # Ekseni kaldırarak temiz görünüm sağla
plt.show()  # Grafiği göster


