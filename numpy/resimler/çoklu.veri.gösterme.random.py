# Çoklu veri(resim) resim gösterme random
import tensorflow as tf, numpy as np, matplotlib.pyplot as plt, random
from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

plt.figure(figsize=(5,5))
def resimleri_goster(veri):
    for n in range(veri):
        ax = plt.subplot(5,5,n+1)
        plt.imshow(x_train[random.randint(0,100)], cmap='gray')
        plt.axis('off')
    plt.show()

resimleri_goster(random.randint(0,25))


