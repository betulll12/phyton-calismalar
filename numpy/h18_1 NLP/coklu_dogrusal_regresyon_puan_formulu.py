# sk-learn ile liste örneğinden puan hesaplama
import pandas as pd, numpy

df = pd.read_csv("h18_1 NLP/lgs_listesi.csv")
df = df.iloc[:,1:len(df)]
# print("\n\ndf.head()\n",df.head())
X = df.drop(['puan','sn','adi_soyadi'],axis=1)

y = df[["puan"]] # pandas dataframe
# print("\n\ny.head()\n",y.head())
# print("\n\nX.head()\n",X.head())

from sklearn.linear_model import LinearRegression
lm = LinearRegression() # LinearRegression
model = lm.fit(X,y)
print("model.intercept_    : ",model.intercept_) # taban katsayısı
print("model.coef_         : ",model.coef_) # bağımsız değişken katsayıları
print("model.score (rkare) : ",model.score(X,y))

tn = int(input("Türkçe netiniz   :"))
mn = int(input("Matematik netiniz:"))
fn = int(input("Fen netiniz      :"))
sn = int(input("Sosyal netiniz   :"))
dn = int(input("Din netiniz      :"))
en = int(input("İnglizce netiniz :"))
netler = [[tn],[mn],[fn],[sn],[dn],[en]]
netler = pd.DataFrame(netler).T
tes = model.predict(netler) # tes = tahmin edilen sonuç
print("\n\nNetlerinize göre model.predict() ile puan tahmininiz : ",tes)
print(netler)

# metrik kısmı düzeltilecek
# from sklearn.metrics import mean_squared_error
# print("model.score (rkare) : ",model.score(X,y))
# print("model.score (rkare) : ",model.score(netler,tes))
# MSE = mean_squared_error(y,model.predict(X))
# MSE = mean_squared_error(tes,model.predict(netler))
# print("\n\nMSE:",MSE)
# import numpy as np
# RMSE = np.sqrt(MSE)
# print("\nRMSE:",RMSE)
