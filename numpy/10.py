# kendi stopwords listeni kullanma
# https://realpython.com/nltk-nlp-python/
# nltk doğal dil işleme için nltk kuralım
# python -m pip install nltk==3.5
# görselleştirme için matplotlib kuralım
# python -m pip install numpy matplotlib
import nltk
# nltk.download('punkt') # Bir kere yapılması gerek/yeter


from nltk.tokenize import sent_tokenize, word_tokenize

ornek_metin = "Bu gün hava çok güzel. \
    Dışarı çıkıp biraz dolaştım. Arkadaşlarla bir yerde oturduk."

cumleler = sent_tokenize(ornek_metin)
kelimeler = word_tokenize(ornek_metin)

print("\n\ncumleler : \n",cumleler)
print("\n\nkelimeler : \n",kelimeler)

import nltk
# nltk.download('punkt') # Bir kere yapılması gerek/yeter
# nltk.download('punkt_tab') # Bir kere yapılması gerek/yeter

from nltk.tokenize import sent_tokenize, word_tokenize

ornek_metin = """
Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult."""

ornek_metin = "Bu gün hava çok güzel. \
    Dışarı çıkıp biraz dolaştım. Arkadaşlarla bir yerde oturduk."


cumleler = sent_tokenize(ornek_metin)
kelimeler = word_tokenize(ornek_metin)

# print(cumleler)
# print("Kelime listesi: ",kelimeler)

nltk.download("stopwords") # Bir kere indirilmesi gerek/yeterli
from nltk.corpus import stopwords

# stop_words = set(stopwords.words("english")) # stop word = anlamsız kelimeler
# stop_words_tr = set(stopwords.words("turkish")) # stop word = köksüz/anlamsız kelimeler



with open("h18_1 NLP/anlamsizlarset.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Süslü parantezleri ve fazlalıkları temizle
text = text.strip("{} \n")

# Çift tırnak içindeki kelimeleri ayıkla
import re
words = re.findall(r'"(.*?)"', text)

# Set'e dönüştür
stop_words_tr = set(words)

temizlenmis_liste = []
# print("Stop words:",stop_words)
print("\n\nStop words Türkçe:",stop_words_tr)

for kelime in kelimeler:
#    if kelime.casefold() not in stop_words: # casefold ile küçükharfe çevir.
   if kelime.casefold() not in stop_words_tr: # casefold ile küçükharfe çevir.
        temizlenmis_liste.append(kelime)
       
print("\n\nTemizlenmiş liste: ",temizlenmis_liste)



