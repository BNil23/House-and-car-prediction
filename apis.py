from importlib.resources import Resource
from flask import request
from flask_restful import Resource
import pandas as pd
import housePricePredictionModel
import carPricePredictionModel
import jsonify

class HousePricePredictionApi(Resource):

    def get(self):

        # global ilce_ 
        
        # if(ilce_deger == "Arnavutköy"):
        #     ilce_ = 0
        # elif(ilce_deger == "Ataşehir"):
        #     ilce_ = 1
        # elif(ilce_deger == "Avcılar"):
        #     ilce_ = 2
        # elif(ilce_deger == "Bahçelievler"):
        #     ilce_ = 3
        # elif(ilce_deger == "Bakırköy"):
        #     ilce_ = 4
        # elif(ilce_deger == "Bayrampaşa"):
        #     ilce_ = 5
        # elif(ilce_deger == "Bağcılar"):
        #     ilce_ = 6
        # elif(ilce_deger == "Başakşehir"):
        #     ilce_ = 7
        # elif(ilce_deger == "Beykoz"):
        #     ilce_ = 8
        # elif(ilce_deger == "Beylikdüzü"):
        #     ilce_ = 9
        # elif(ilce_deger == "Beyoğlu"):
        #     ilce_ = 10
        # elif(ilce_deger == "Beşiktaş"):
        #     ilce_ = 11
        # elif(ilce_deger == "Büyükçekmece"):
        #     ilce_ = 12
        # elif(ilce_deger == "Esenler"):
        #     ilce_ = 13
        # elif(ilce_deger == "Esenyurt"):
        #     ilce_ = 14
        # elif(ilce_deger == "Eyüpsultan"):
        #     ilce_ = 15
        # elif(ilce_deger == "Fatih"):
        #     ilce_ = 16
        # elif(ilce_deger == "Gaziosmanpaşa"):
        #     ilce_ = 17
        # elif(ilce_deger == "Güngören"):
        #     ilce_ = 18
        # elif(ilce_deger == "Kadıköy"):
        #     ilce_ = 19
        # elif(ilce_deger == "Kartal"):
        #     ilce_ = 20
        # elif(ilce_deger == "Kağıthane"):
        #     ilce_ = 21
        # elif(ilce_deger == "Küçükçekmece"):
        #     ilce_ = 22
        # elif(ilce_deger == "Maltepe"):
        #     ilce_ = 23
        # elif(ilce_deger == "Pendik"):
        #     ilce_ = 24
        # elif(ilce_deger == "Sancaktepe"):
        #     ilce_ = 25
        # elif(ilce_deger == "Sarıyer"):
        #     ilce_ = 26
        # elif(ilce_deger == "Silivri"):
        #     ilce_ = 27
        # elif(ilce_deger == "Sultanbeyli"):
        #     ilce_ = 28
        # elif(ilce_deger == "Tuzla"):
        #     ilce_ = 29
        # elif(ilce_deger == "Zeytinburnu"):
        #     ilce_ = 30
        # elif(ilce_deger == "Çekmeköy"):
        #     ilce_ = 31
        # elif(ilce_deger == "Ümraniye"):
        #     ilce_ = 32
        # elif(ilce_deger == "Üsküdar"):
        #     ilce_ = 33
        # elif(ilce_deger == "Şişli"):
        #     ilce_ = 34  

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

        # print(args['ilce_deger'])
        # print(args['net_deger'])
        # print(args['brut_deger'])
        # print(args['oda_deger'])
        # print(args['yas_deger'])
        # print(args['kat_deger'])

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

        pred = housePricePredictionModel.model_xgb.predict(df_2)

        return str(pred) 

class CarPricePredictionApi(Resource):

    def get(self):

        args = request.args

        marka = int(args['marka'])
        seri = int(args['seri'])
        yil = int(args['yil'])
        yakit = int(args['yakit'])
        vites = int(args['vites'])
        motorh = int(args['motor_hacmi'])
        motorg = int(args['motor_gucu'])
        km = int(args['km'])
        tramer = int(args['tramer'])

        yeni_veri = [[marka], [seri], [yil], [yakit], [vites], [motorh], [motorg], [km], [tramer]]
        yeni_veri = pd.DataFrame(yeni_veri).T
        
        df_2 = yeni_veri.rename(columns = {0:"Marka",
                            1:"Seri",
                            2:"Yıl",
                            3:"Yakıt Tipi",
                            4:"Vites Tipi",
                            5:"Motor Hacmi",
                            6:"Motor Gücü",
                            7:"Kilometre",
                            8:"Toplam Tramer Tutarı"})

        pred = carPricePredictionModel.model_xgb.predict(df_2)
    
        return str(pred)