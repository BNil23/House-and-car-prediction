from importlib.resources import Resource
# from urllib import request
from flask import request
from flask_restful import Api, Resource, reqparse
from sklearn.model_selection import train_test_split, GridSearchCV,cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn import preprocessing
import numpy as np
import pandas as pd
import xgboost as xgb
from xgboost import XGBRegressor

parser = reqparse.RequestParser()

class LinearRegressionApi(Resource):

    def get(self):

        # parser.add_argument('ilce_deger', type = int)
        # parser.add_argument('net_deger', type = int)
        # parser.add_argument('brut_deger', type = int)
        # parser.add_argument('yas_deger', type = int)
        # parser.add_argument('kat_deger', type = int)
        # parser.add_argument('oda_deger', type = int)
        # args = parser.parse_args()

        df = pd.read_csv("emlak_verisi.csv")
        df.drop("Sehir", axis = 1, inplace = True)
        df.drop("Mahalle", axis = 1, inplace = True)
        df.dropna(inplace = True)

        df = df[["İlce","Fiyat","brüt metrekare","Net Metrekare","Oda Sayısı","Binanın Yaşı","Bulunduğu Kat"]]

        X = df.drop(["Fiyat"], axis = 1)
        y = df["Fiyat"] 

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 144)
        params = {"colsample_bytree":[0.4,0.5,0.6],
         "learning_rate":[0.01,0.02,0.09],
         "max_depth":[2,3,4,5,6],
         "n_estimators":[100,200,500,2000]}
        xgb = XGBRegressor()
        grid = GridSearchCV(xgb, params, cv = 10, n_jobs = -1, verbose = 2)
        grid.fit(X_train, y_train)
        
        xgb1 = XGBRegressor(colsample_bytree = grid.best_params_["colsample_bytree"], 
                            learning_rate = grid.best_params_["learning_rate"], 
                            max_depth = grid.best_params_["max_depth"], 
                            n_estimators = grid.best_params_["n_estimators"])
        
        model_xgb = xgb1.fit(X_train, y_train)
        
        # global ilce 
        
        # if(ilce_deger == "Arnavutköy"):
        #     ilce = 0
        # elif(ilce_deger == "Ataşehir"):
        #     ilce = 1
        # elif(ilce_deger == "Avcılar"):
        #     ilce = 2
        # elif(ilce_deger == "Bahçelievler"):
        #     ilce = 3
        # elif(ilce_deger == "Bakırköy"):
        #     ilce = 4
        # elif(ilce_deger == "Bayrampaşa"):
        #     ilce = 5
        # elif(ilce_deger == "Bağcılar"):
        #     ilce = 6
        # elif(ilce_deger == "Başakşehir"):
        #     ilce = 7
        # elif(ilce_deger == "Beykoz"):
        #     ilce = 8
        # elif(ilce_deger == "Beylikdüzü"):
        #     ilce = 9
        # elif(ilce_deger == "Beyoğlu"):
        #     ilce = 10
        # elif(ilce_deger == "Beşiktaş"):
        #     ilce = 11
        # elif(ilce_deger == "Büyükçekmece"):
        #     ilce = 12
        # elif(ilce_deger == "Esenler"):
        #     ilce = 13
        # elif(ilce_deger == "Esenyurt"):
        #     ilce = 14
        # elif(ilce_deger == "Eyüpsultan"):
        #     ilce = 15
        # elif(ilce_deger == "Fatih"):
        #     ilce = 16
        # elif(ilce_deger == "Gaziosmanpaşa"):
        #     ilce = 17
        # elif(ilce_deger == "Güngören"):
        #     ilce = 18
        # elif(ilce_deger == "Kadıköy"):
        #     ilce = 19
        # elif(ilce_deger == "Kartal"):
        #     ilce = 20
        # elif(ilce_deger == "Kağıthane"):
        #     ilce = 21
        # elif(ilce_deger == "Küçükçekmece"):
        #     ilce = 22
        # elif(ilce_deger == "Maltepe"):
        #     ilce = 23
        # elif(ilce_deger == "Pendik"):
        #     ilce = 24
        # elif(ilce_deger == "Sancaktepe"):
        #     ilce = 25
        # elif(ilce_deger == "Sarıyer"):
        #     ilce = 26
        # elif(ilce_deger == "Silivri"):
        #     ilce = 27
        # elif(ilce_deger == "Sultanbeyli"):
        #     ilce = 28
        # elif(ilce_deger == "Tuzla"):
        #     ilce = 29
        # elif(ilce_deger == "Zeytinburnu"):
        #     ilce = 30
        # elif(ilce_deger == "Çekmeköy"):
        #     ilce = 31
        # elif(ilce_deger == "Ümraniye"):
        #     ilce = 32
        # elif(ilce_deger == "Üsküdar"):
        #     ilce = 33
        # elif(ilce_deger == "Şişli"):
        #     ilce = 34  

        # brut = brut_deger
        
        # net = net_deger
        
        # global oda
        
        # if(oda_deger == '1 Oda' ):
        #     oda = 0
        # elif(oda_deger == '1+1'):
        #     oda = 1
        # elif(oda_deger == '2+0'):
        #     oda = 2
        # elif(oda_deger == '2+1'):
        #     oda = 3
        # elif(oda_deger == '2+2'):
        #     oda = 4
        # elif(oda_deger == '3+1'):
        #     oda = 5
        # elif(oda_deger == '3+2'):
        #     oda = 6
        # elif(oda_deger == '3.5+1'):
        #     oda = 7
        # elif(oda_deger == '4+1'):
        #     oda = 8
        # elif(oda_deger == '4+2'):
        #     oda = 9
        # elif(oda_deger == '5+1'):
        #     oda = 10    
        # elif(oda_deger == '5+2'):
        #     oda = 11
        # elif(oda_deger == '5+3'):
        #     oda = 12
        # elif(oda_deger == '6+1'):
        #     oda = 13
        # elif(oda_deger == '6+2'):
        #     oda = 14
        # elif(oda_deger == '6+3'):
        #     oda = 15
        # elif(oda_deger == '7+2'):
        #     oda = 16
        # elif(oda_deger == '8+ Oda'):
        #     oda = 17
        # elif(oda_deger == 'Stüdyo'):
        #     oda = 18

        # global yas
        
        # if(yas_deger == '0 (Yeni)'):
        #     yas = 0
        # elif(yas_deger == '1'):
        #     yas = 1
        # elif(yas_deger == '11-15'):
        #     yas = 2
        # elif(yas_deger == '16-20'):
        #     yas = 3
        # elif(yas_deger == '2'):
        #     yas = 4
        # elif(yas_deger == '21 Ve Üzeri'):
        #     yas = 5
        # elif(yas_deger == '3'):
        #     yas = 6
        # elif(yas_deger == '4'):
        #     yas = 7
        # elif(yas_deger == '5-10'):
        #     yas = 8
            
        # global kat
        
        # if(kat_deger == '1'):
        #     kat = 0
        # elif(kat_deger == '10'):
        #     kat = 1
        # elif(kat_deger == '11'):
        #     kat = 2
        # elif(kat_deger == '12'):
        #     kat = 3
        # elif(kat_deger == '13'):
        #     kat = 4
        # elif(kat_deger == '15'):
        #     kat = 5
        # elif(kat_deger == '18'):
        #     kat = 6
        # elif(kat_deger == '2'):
        #     kat = 7
        # elif(kat_deger == '20'):
        #     kat = 8
        # elif(kat_deger == '21'):
        #     kat = 9
        # elif(kat_deger == '28'):
        #     kat = 10
        # elif(kat_deger == '3'):
        #     kat = 11
        # elif(kat_deger == '4'):
        #     kat = 12
        # elif(kat_deger == '5'):
        #     kat = 13
        # elif(kat_deger == '6'):
        #     kat = 14
        # elif(kat_deger == '7'):
        #     kat = 15
        # elif(kat_deger == '8'):
        #     kat = 16
        # elif(kat_deger == '9'):
        #     kat = 17
        # elif(kat_deger == 'Bahçe Dublex'):
        #     kat = 18
        # elif(kat_deger == 'Bahçe Katı'):
        #     kat = 19
        # elif(kat_deger == 'Düz Giriş'):
        #     kat = 10
        # elif(kat_deger == 'Kot 1 (-1)'):
        #     kat = 11
        # elif(kat_deger == 'Kot 3 (-3)'):
        #     kat = 12
        # elif(kat_deger == 'Müstakil'):
        #     kat = 12
        # elif(kat_deger == 'Villa Tipi'):
        #     kat = 13
        # elif(kat_deger == 'Yüksek Giriş'):
        #     kat = 14
        # elif(kat_deger == 'Çatı Dubleks'):
        #     kat = 15
        # elif(kat_deger == 'Çatı Katı'):
        #     kat = 16

        args = request.args

        ilce = int(args['ilce_deger'])
        net = int(args['net_deger'])
        brut = int(args['brut_deger'])
        oda = int(args['oda_deger'])
        yas = int(args['yas_deger'])
        kat = int(args['kat_deger'])

        yeni_veri = [[ilce], [net], [brut], [oda], [yas], [kat]]    
        yeni_veri = pd.DataFrame(yeni_veri).T

        df_2 = yeni_veri.rename(columns = {0:"İlce",
                            1:"brüt metrekare",
                            2:"Net Metrekare",
                            3:"Oda Sayısı",
                            4:"Binanın Yaşı",
                            5:"Bulunduğu Kat"})

        pred = model_xgb.predict(df_2)
    
        # if(pred < 0):
        #     pred = (-1) * pred
        
        # pred = int(pred)

        return str(pred) 


