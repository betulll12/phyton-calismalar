# https://realpython.com/nltk-nlp-python/
# nltk doğal dil işleme için nltk kuralım
# python -m pip install nltk==3.5
# görselleştirme için matplotlib kuralım
# python -m pip install numpy matplotlib
import nltk
# nltk.download('punkt') # Bir kere yapılması gerek/yeter
import nltk
nltk.download('punkt_tab')



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


print("\n\ncumleler : \n",cumleler)
print("\n\nkelimeler : \n",kelimeler)
