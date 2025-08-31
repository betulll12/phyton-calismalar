mail_gonderilecekler = [
    "Uğur KARA",
    "Reyhan BUDAK",
    "Öznur KAYA",
    "Beyza DEMİR"
]

def fonksiyon1(gelen):
    return f"Sayın: {gelen}"

# print(*list(map(fonksiyon1, mail_gonderilecekler)), sep="\n")
yeni_liste = list(map(fonksiyon1, mail_gonderilecekler))
for a in yeni_liste:
    print(a)
