import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import statsmodels.api as sm

class CreateModel:
    def __init__(self, X, y):

        self.data = pd.read_csv('data.csv')

        # self.X = np.array(X)
        # self.y = np.array(y)
        # print(self.X)
        # print(self.y)

    def train_model(self):
        # self.Le = LabelEncoder()
        # for i in range(len(self.X[0]) - 1):
        #     self.X[:, i] = self.Le.fit_transform(self.X[:, i])
        # #X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size = 0.2)
        #
        # print(self.X)
        # self.X[:, 2] = int(self.X[:, 2])
        # self.y[:] = int(self.y[:])
        # self.model = linear_model.LinearRegression()
        # self.model.fit(np.array(self.X), self.y)
     print(self.data)

    def predict(self):

        mb = input("brüt metrekare")
        mn = input("Net Metrekare")
        os = input('Oda Sayısı')
        by = input('Binanın Yaşı')
        bk = input('Bulunduğu Kat')
        bs2 = input('Banyo Sayısı')
        ts = input('WC Sayısı')
        si = input('Site İçerisinde')
        bd = input('Balkon Durumu')
        yt = input('Yapı Tipi')
        bs3 = input('Balkon Sayısı')
        sehir = input('Sehir')
        ilce = input('İlce')
        mahalle = input('Mahalle')
        price = input('Fiyat')

        inp = [mb, mn, os, by, bk, bs2, ed, si, bd, yt, bs3, sehir, ilce, mahalle, price]
        r_inp = self.Le.transform(inp)
        #list(r_inp).append(int())
        predictions = self.model.predict(np.array(r_inp))
        print(predictions)

