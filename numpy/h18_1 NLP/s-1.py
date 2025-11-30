# Veri üzere değerleri ekleyelim
import tensorflow as tf, numpy as np, matplotlib.pyplot as plt, random
# import warnings; warnings.filterwarnings("ignore")
from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data() # x_train : 28x28 eğitim görselleri, y_train görüntü etiketleri


def resim_uzerinde_deger_göster(resim):
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    ax.imshow(resim, cmap='gray')
   
    genislik, yukseklik = resim.shape  
    esik = resim.max() / 2.5  
    for x in range(genislik):
        for y in range(yukseklik):
            ax.annotate(
                str(round(resim[x, y], 2)),
                xy=(y, x),
                color="blue" if y % 2 == 0 else 'red',
                ha="center", va="center", fontsize=7  # # Ortalamak ve küçült
            )    
    plt.show()


resim_uzerinde_deger_göster(x_train[0])
resim_uzerinde_deger_göster(x_train[random.randint(0,len(x_train)-1)])


