class Ogrenci():  # Sınıf isimleri büyük harf ile başlar.
    ogrenci_no = "__"  # ogrenci_no /prop/property/özellik
    adi_soyadi = "Tanımsız"
    sinifi = "__"
    disiplin_puani = "100"

ogrenci1 = Ogrenci()  # sınıftan nesne çoğaltma/oluşturma işlemi. Parantezler çok önemli
ogrenci2 = Ogrenci()  # sınıftan nesne çoğaltma/oluşturma işlemi. Parantezler çok önemli

ogrenci1.adi_soyadi = "Öznur KARA"
ogrenci2.adi_soyadi = "Reyhan KAYA"

print(ogrenci1.adi_soyadi, ogrenci2.adi_soyadi)
