# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 01:34:45 2020

@author: Ozgur Kucet
"""
from math import sqrt

def ortalama(liste):
    toplam = 0
    for i in liste:
        toplam+=i
    return toplam/len(liste)

def StandartSapma(liste):
    ortalama1 = ortalama(liste)
    ListeEksiOrt = []
    for i in liste:
        ListeEksiOrt.append(i-ortalama1)
    listeEksiOrtKare = []    
    for i in ListeEksiOrt:
        listeEksiOrtKare.append(i*i)
    ListeEksiOrtKareToplam = 0
    for i in listeEksiOrtKare:
        ListeEksiOrtKareToplam += i
    print(ListeEksiOrtKareToplam)
    
    return sqrt(ListeEksiOrtKareToplam/(len(liste)-1))


liste = [3,3,4,6,9]
print(StandartSapma(liste))

