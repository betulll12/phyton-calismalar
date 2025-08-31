open  ("deneme1.py","a")
dosya = open("deneme3.txt","w")  # w modu ile dosya yoksa oluşur, varsa içine dekil...
dosya.write("Betül MUTLU, 05089854785\n")
dosya.write("Beyza Ali, 085856325478\n")

dosya.close()  # dosyalarını kapatarak bir çok hatanın önlemini alın.
