# pip install matplotlib
import matplotlib.pyplot as plt
# plt.plot([1,2,3], [80,70,90])
# plt.bar([1,2,3], [80,70,90])
# plt.pie([80,70,90])
kategoriler = ["1.Sınav","2.Sınav","3.Sınav"]
degerler = [80,70,90]
plt.bar(kategoriler, degerler)
plt.show()
