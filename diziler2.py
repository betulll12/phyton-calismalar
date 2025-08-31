meyveler1 = ['Elma', 'Nar', 'Portakal', 'Muz', 'Goz']  # list
meyveler2 = ('Nar', 'Portakal', 'Muz', 'Goz', 'Elma')  # tuple

print(meyveler1)  # Boş Listeyi ekrana yazdırır
print(meyveler2)  # Boş Listeyi ekrana yazdırır

print("Dizi uzunluğu: ", len(meyveler1))

meyveler1.append("Dut")
# meyveler2.append("Dut")  # tuple lara ekleme yapılamaz.
meyveler2 += ("Dut",)  # += ile ekleme yapılabilir. Sondaki , önemli.
print(meyveler1)  # Boş Listeyi ekrana yazdırır
print(meyveler2)  # Boş Listeyi ekrana yazdırır
print(type((['Elma', 'Nar', 'Portakal','Muz', 'Goz'])))
print(type(meyveler2))
abc = {"ad":"Ali","tel":"05076325874",44:"aaa",55:23,33:["5","8"]} # key:value
print(abc)

print("1 indexli eleman:",meyveler1[1])  # index değeri 1.
print("1 indexli eleman:",meyveler2[1])  # index değeri 1.
# print("1 indexli eleman:",abc[1])  # index değeri 1. # Hata verir. dict de index olmaz.
print("ad keyli  eleman:",abc["ad"])     # index değeri 1.
print("ad keyli  eleman:",abc[44])       # index değeri 1.
print("ad keyli  eleman:",abc[55])       # index değeri 1.
print("ad keyli  eleman:",abc[33])       # index değeri 1.
print("ad keyli  eleman:",abc[33][1])    # index değeri 1.
