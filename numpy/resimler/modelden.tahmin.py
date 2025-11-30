# MODELDEN TAHMİN
import tensorflow as tf, numpy as np, matplotlib.pyplot as plt
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt


from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data() # x_train : 28x28 eğitim görselleri, y_train görüntü etiketleri




model = tf.keras.models.load_model('mnist_model.h5')
import random
# rasgele = random.randint(0, x_test.shape[0])
rasgele = random.randint(0, 100)


print ("rastgele: ",rasgele)
ornek_resim = x_test[rasgele]
print ("y_test[rastgele]: ",y_test[rasgele])


plt.imshow(ornek_resim.reshape(28,28),cmap = 'gray')
plt.show()


test_verisi = x_test[rasgele].reshape(1,28,28,1)
ihtimal = model.predict(test_verisi)


tahmin_edilen_siniflar = np.argmax(ihtimal)


print(f"Tahmin edilen sınıf: {tahmin_edilen_siniflar}")
print(f"Tahmin edilen sınıfın olasılık değeri: {(np.max(ihtimal, axis=-1))[0]}\n")
print(f"Diğer sınıfların olasılık değerleri: {ihtimal}")


plt.imshow(ornek_resim.reshape(28,28),cmap = 'gray')
plt.show()


print('rasgele:', rasgele)
print('y_test[rasgele]:', y_test[rasgele])
