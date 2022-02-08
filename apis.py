from importlib.resources import Resource
from flask import request
from flask_restful import Resource
import pandas as pd
import housePricePredictionModel
import carPricePredictionModel

class HousePricePredictionApi(Resource):

    def get(self):
        
        args = request.args

        ilce_deger = str(args['ilce_deger'])
        net_deger = int(args['net_deger'])
        brut_deger = int(args['brut_deger'])
        oda_deger = str(args['oda_deger'])
        yas_deger = str(args['yas_deger'])
        kat_deger = str(args['kat_deger'])

        global ilce_ 
        
        if(ilce_deger == "Arnavutköy"):
            ilce_ = 0
        elif(ilce_deger == "Ataşehir"):
            ilce_ = 1
        elif(ilce_deger == "Avcılar"):
            ilce_ = 2
        elif(ilce_deger == "Bahçelievler"):
            ilce_ = 3
        elif(ilce_deger == "Bakırköy"):
            ilce_ = 4
        elif(ilce_deger == "Bayrampaşa"):
            ilce_ = 5
        elif(ilce_deger == "Bağcılar"):
            ilce_ = 6
        elif(ilce_deger == "Başakşehir"):
            ilce_ = 7
        elif(ilce_deger == "Beykoz"):
            ilce_ = 8
        elif(ilce_deger == "Beylikdüzü"):
            ilce_ = 9
        elif(ilce_deger == "Beyoğlu"):
            ilce_ = 10
        elif(ilce_deger == "Beşiktaş"):
            ilce_ = 11
        elif(ilce_deger == "Büyükçekmece"):
            ilce_ = 12
        elif(ilce_deger == "Esenler"):
            ilce_ = 13
        elif(ilce_deger == "Esenyurt"):
            ilce_ = 14
        elif(ilce_deger == "Eyüpsultan"):
            ilce_ = 15
        elif(ilce_deger == "Fatih"):
            ilce_ = 16
        elif(ilce_deger == "Gaziosmanpaşa"):
            ilce_ = 17
        elif(ilce_deger == "Güngören"):
            ilce_ = 18
        elif(ilce_deger == "Kadıköy"):
            ilce_ = 19
        elif(ilce_deger == "Kartal"):
            ilce_ = 20
        elif(ilce_deger == "Kağıthane"):
            ilce_ = 21
        elif(ilce_deger == "Küçükçekmece"):
            ilce_ = 22
        elif(ilce_deger == "Maltepe"):
            ilce_ = 23
        elif(ilce_deger == "Pendik"):
            ilce_ = 24
        elif(ilce_deger == "Sancaktepe"):
            ilce_ = 25
        elif(ilce_deger == "Sarıyer"):
            ilce_ = 26
        elif(ilce_deger == "Silivri"):
            ilce_ = 27
        elif(ilce_deger == "Sultanbeyli"):
            ilce_ = 28
        elif(ilce_deger == "Tuzla"):
            ilce_ = 29
        elif(ilce_deger == "Zeytinburnu"):
            ilce_ = 30
        elif(ilce_deger == "Çekmeköy"):
            ilce_ = 31
        elif(ilce_deger == "Ümraniye"):
            ilce_ = 32
        elif(ilce_deger == "Üsküdar"):
            ilce_ = 33
        elif(ilce_deger == "Şişli"):
            ilce_ = 34  

        brut = brut_deger
        
        net = net_deger
        
        global oda
        
        if(oda_deger == '1 Oda' ):
            oda = 0
        elif(oda_deger == '1+1'):
            oda = 1
        elif(oda_deger == '2+0'):
            oda = 2
        elif(oda_deger == '2+1'):
            oda = 3
        elif(oda_deger == '2+2'):
            oda = 4
        elif(oda_deger == '3+1'):
            oda = 5
        elif(oda_deger == '3+2'):
            oda = 6
        elif(oda_deger == '3.5+1'):
            oda = 7
        elif(oda_deger == '4+1'):
            oda = 8
        elif(oda_deger == '4+2'):
            oda = 9
        elif(oda_deger == '5+1'):
            oda = 10    
        elif(oda_deger == '5+2'):
            oda = 11
        elif(oda_deger == '5+3'):
            oda = 12
        elif(oda_deger == '6+1'):
            oda = 13
        elif(oda_deger == '6+2'):
            oda = 14
        elif(oda_deger == '6+3'):
            oda = 15
        elif(oda_deger == '7+2'):
            oda = 16
        elif(oda_deger == '8+ Oda'):
            oda = 17
        elif(oda_deger == 'Stüdyo'):
            oda = 18

        global yas
        
        if(yas_deger == '0 (Yeni)'):
            yas = 0
        elif(yas_deger == '1'):
            yas = 1
        elif(yas_deger == '11-15'):
            yas = 2
        elif(yas_deger == '16-20'):
            yas = 3
        elif(yas_deger == '2'):
            yas = 4
        elif(yas_deger == '21 Ve Üzeri'):
            yas = 5
        elif(yas_deger == '3'):
            yas = 6
        elif(yas_deger == '4'):
            yas = 7
        elif(yas_deger == '5-10'):
            yas = 8
            
        global kat
        
        if(kat_deger == '1'):
            kat = 0
        elif(kat_deger == '10'):
            kat = 1
        elif(kat_deger == '11'):
            kat = 2
        elif(kat_deger == '12'):
            kat = 3
        elif(kat_deger == '13'):
            kat = 4
        elif(kat_deger == '15'):
            kat = 5
        elif(kat_deger == '18'):
            kat = 6
        elif(kat_deger == '2'):
            kat = 7
        elif(kat_deger == '20'):
            kat = 8
        elif(kat_deger == '21'):
            kat = 9
        elif(kat_deger == '28'):
            kat = 10
        elif(kat_deger == '3'):
            kat = 11
        elif(kat_deger == '4'):
            kat = 12
        elif(kat_deger == '5'):
            kat = 13
        elif(kat_deger == '6'):
            kat = 14
        elif(kat_deger == '7'):
            kat = 15
        elif(kat_deger == '8'):
            kat = 16
        elif(kat_deger == '9'):
            kat = 17
        elif(kat_deger == 'Bahçe Dublex'):
            kat = 18
        elif(kat_deger == 'Bahçe Katı'):
            kat = 19
        elif(kat_deger == 'Düz Giriş'):
            kat = 10
        elif(kat_deger == 'Kot 1 (-1)'):
            kat = 11
        elif(kat_deger == 'Kot 3 (-3)'):
            kat = 12
        elif(kat_deger == 'Müstakil'):
            kat = 12
        elif(kat_deger == 'Villa Tipi'):
            kat = 13
        elif(kat_deger == 'Yüksek Giriş'):
            kat = 14
        elif(kat_deger == 'Çatı Dubleks'):
            kat = 15
        elif(kat_deger == 'Çatı Katı'):
            kat = 16

        # print(args['ilce_deger'])
        # print(args['net_deger'])
        # print(args['brut_deger'])
        # print(args['oda_deger'])
        # print(args['yas_deger'])
        # print(args['kat_deger'])

        ilce = ilce_
        net = net
        brut = brut
        oda = oda
        yas = yas
        kat = kat

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

        marka_deger = str(args['marka_deger'])
        seri_deger = str(args['seri_deger'])
        yil_deger = int(args['yil_deger'])
        yakit_deger = str(args['yakit_tipi'])
        vites_deger = str(args['vites_tipi'])
        motorHacmi_deger = int(args['motor_hacmi'])
        motorGucu_deger = int(args['motor_gucu'])
        km_deger = int(args['km_deger'])
        tramer_deger = int(args['tramer_deger'])

        global marka
    
        if(marka_deger == "Audi"):
            marka = 0
        elif(marka_deger == "BMW"):
            marka = 1
        elif(marka_deger == "Chevrolet"):
            marka = 2
        elif(marka_deger == "Citroen"):
            marka = 3
        elif(marka_deger == "Dacia"):
            marka = 4
        elif(marka_deger == "Fiat"):
            marka = 5
        elif(marka_deger == "Ford"):
            marka = 6
        elif(marka_deger == "Honda"):
            marka = 7
        elif(marka_deger == "Hyundai"):
            marka = 8
        elif(marka_deger == "Infiniti"):
            marka = 9
        elif(marka_deger == "Jaguar"):
            marka = 10
        elif(marka_deger == "Kia"):
            marka = 11
        elif(marka_deger == "Lada"):
            marka = 12
        elif(marka_deger == "MINI"):
            marka = 13
        elif(marka_deger == "Maserati"):
            marka = 14
        elif(marka_deger == "Mercedes - Benz"):
            marka = 15
        elif(marka_deger == "Nissan"):
            marka = 16
        elif(marka_deger == "Opel"):
            marka = 17
        elif(marka_deger == "Peugeot"):
            marka = 18
        elif(marka_deger == "Porsche"):
            marka = 19
        elif(marka_deger == "Renault"):
            marka = 20
        elif(marka_deger == "Seat"):
            marka = 21
        elif(marka_deger == "Skoda"):
            marka = 22
        elif(marka_deger == "Tofaş"):
            marka = 23
        elif(marka_deger == "Toyota"):
            marka = 24
        elif(marka_deger == "Volkswagen"):
            marka = 25
        elif(marka_deger == "Volvo"):
            marka = 26
  

        global seri 
        
        if(seri_deger == "1 Serisi"):
            seri = 0
        elif(seri_deger == "200"):
            seri = 1
        elif(seri_deger == "206"):
            seri = 2
        elif(seri_deger == "207"):
            seri = 3
        elif(seri_deger == "208"):
            seri = 4
        elif(seri_deger == "3 Serisi"):
            seri = 5
        elif(seri_deger == "300"):
            seri = 6
        elif(seri_deger == "301"):
            seri = 7
        elif(seri_deger == "308"):
            seri = 8
        elif(seri_deger == "5 Serisi"):
            seri = 9
        elif(seri_deger == "508"):
            seri = 10
        elif(seri_deger == "A"):
            seri = 11
        elif(seri_deger == "A3"):
            seri = 12
        elif(seri_deger == "A4"):
            seri = 13
        elif(seri_deger == "A6"):
            seri = 14
        elif(seri_deger == "Accent"):
            seri = 15
        elif(seri_deger == "Accent Blue"):
            seri = 16
        elif(seri_deger == "Accent Era"):
            seri = 17
        elif(seri_deger == "Accord"):
            seri = 18
        elif(seri_deger == "Albea"):
            seri = 19
        elif(seri_deger == "Arteon"):
            seri = 20
        elif(seri_deger == "Astra"):
            seri = 21
        elif(seri_deger == "Auris"):
            seri = 22
        elif(seri_deger == "Aveo"):
            seri = 23
        elif(seri_deger == "B"):
            seri = 24
        elif(seri_deger == "Bora"):
            seri = 25
        elif(seri_deger == "Bravo"):
            seri = 26
        elif(seri_deger == "C"):
            seri = 27
        elif(seri_deger == "C-Elysee"):
            seri = 28
        elif(seri_deger == "C-Max"):
            seri = 29
        elif(seri_deger == "C3"):
            seri = 30
        elif(seri_deger == "C4"):
            seri = 31
        elif(seri_deger == "C5"):
            seri = 32
        elif(seri_deger == "CLA"):
            seri = 33
        elif(seri_deger == "Ceed"):
            seri = 34
        elif(seri_deger == "Cerato"):
            seri = 35
        elif(seri_deger == "City"):
            seri = 36
        elif(seri_deger == "Civic"):
            seri = 37
        elif(seri_deger == "Clio"):
            seri = 38
        elif(seri_deger == "Cooper"):
            seri = 39
        elif(seri_deger == "Corolla"):
            seri = 40
        elif(seri_deger == "Corsa"):
            seri = 41
        elif(seri_deger == "Cruze"):
            seri = 42
        elif(seri_deger == "Doğan"):
            seri = 43
        elif(seri_deger == "E"):
            seri = 44
        elif(seri_deger == "Egea"):
            seri = 45
        elif(seri_deger == "Elantra"):
            seri = 46
        elif(seri_deger == "Favorit"):
            seri = 47
        elif(seri_deger == "Fiesta"):
            seri = 48
        elif(seri_deger == "Fluence"):
            seri = 49
        elif(seri_deger == "Focus"):
            seri = 50
        elif(seri_deger == "Getz"):
            seri = 51
        elif(seri_deger == "Ghibli"):
            seri = 52
        elif(seri_deger == "Golf"):
            seri = 53
        elif(seri_deger == "Ibiza"):
            seri = 54
        elif(seri_deger == "Insignia"):
            seri = 55
        elif(seri_deger == "Jetta"):
            seri = 56
        elif(seri_deger == "Kalos"):
            seri = 57
        elif(seri_deger == "Kartal"):
            seri = 58
        elif(seri_deger == "Lacetti"):
            seri = 59
        elif(seri_deger == "Latitude"):
            seri = 60
        elif(seri_deger == "Leon"):
            seri = 61
        elif(seri_deger == "Linea"):
            seri = 62
        elif(seri_deger == "Logan"):
            seri = 63
        elif(seri_deger == "M Serisi"):
            seri = 64
        elif(seri_deger == "Megane"):
            seri = 65
        elif(seri_deger == "Micra"):
            seri = 66
        elif(seri_deger == "Mondeo"):
            seri = 67
        elif(seri_deger == "New Beetle"):
            seri = 68
        elif(seri_deger == "Octavia"):
            seri = 69
        elif(seri_deger == "Palio"):
            seri = 70
        elif(seri_deger == "Panamera"):
            seri = 71
        elif(seri_deger == "Passat"):
            seri = 72
        elif(seri_deger == "Passat Variant"):
            seri = 73
        elif(seri_deger == "Polo"):
            seri = 74
        elif(seri_deger == "Primera"):
            seri = 75
        elif(seri_deger == "Punto"):
            seri = 76
        elif(seri_deger == "Q50"):
            seri = 77
        elif(seri_deger == "R 12"):
            seri = 78
        elif(seri_deger == "R 19"):
            seri = 79
        elif(seri_deger == "R 9"):
            seri = 80
        elif(seri_deger == "Rapid"):
            seri = 81
        elif(seri_deger == "Rio"):
            seri = 82
        elif(seri_deger == "S60"):
            seri = 83
        elif(seri_deger == "S90"):
            seri = 84
        elif(seri_deger == "SLK"):
            seri = 85
        elif(seri_deger == "Samara"):
            seri = 86
        elif(seri_deger == "Sandero"):
            seri = 87
        elif(seri_deger == "Scala"):
            seri = 88
        elif(seri_deger == "Scenic"):
            seri = 89
        elif(seri_deger == "Scirocco"):
            seri = 90
        elif(seri_deger == "Stilo"):
            seri = 91
        elif(seri_deger == "SuperB"):
            seri = 92
        elif(seri_deger == "Symbol"):
            seri = 93
        elif(seri_deger == "Tempra"):
            seri = 94
        elif(seri_deger == "Tipo"):
            seri = 95
        elif(seri_deger == "Toledo"):
            seri = 96
        elif(seri_deger == "Uno"):
            seri = 97
        elif(seri_deger == "VW CC"):
            seri = 98
        elif(seri_deger == "Vectra"):
            seri = 99
        elif(seri_deger == "XF"):
            seri = 100
        elif(seri_deger == "Yaris"):
            seri = 101
        elif(seri_deger == "i20"):
            seri = 102
        elif(seri_deger == "i30"):
            seri = 103
        elif(seri_deger == "Şahin"):
            seri = 104
            

        yil = yil_deger   
                
                
        global yakit
        
        if(yakit_deger == "Benzin"):
            yakit = 0
        elif(yakit_deger == "Dizel"):
            yakit = 1
        elif(yakit_deger == "LPG & Benzin"):
            yakit = 2
        
    
        global vites 
        
        if(vites_deger == "Düz"):
            vites = 0
        elif(vites_deger == "Otomatik"):
            vites = 1
        elif(vites_deger == "Yarı Otomatik"):
            vites = 2

        motorh = motorHacmi_deger
        motorg = motorGucu_deger
        km = km_deger
        tramer = tramer_deger

        yeni_veri = [[marka], [seri], [yil], [yakit], [vites], [motorh], [motorg], [km], [tramer]]
        yeni_veri = pd.DataFrame(yeni_veri).T
        
        df_2 = yeni_veri.rename(columns = {0:"Marka",
                            1:"Seri",
                            2:"Model",
                            3:"Yıl",
                            4:"Yakıt Tipi",
                            5:"Vites Tipi",
                            6:"Motor Hacmi",
                            7:"Motor Gücü",
                            8:"Kilometre",
                            9:"Toplam Tramer Tutarı"})

        pred = carPricePredictionModel.model_xgb.predict(df_2)
    

        return pred