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
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

