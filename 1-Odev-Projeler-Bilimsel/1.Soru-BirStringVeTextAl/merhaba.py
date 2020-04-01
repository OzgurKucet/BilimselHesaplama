# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 04:06:23 2020

@author: Ozgur Kucet


** Bir string ve bir text alıcak string textte varsa true yoksa false
* bir string ve bir text alıcak string textte varsa var ve şurada diyecek
* ikinci gönderilen parametre 1. parametreden n defa bulunuyorsa bulunduğu 
* yerlerin başlangıç adresini liste halinde geri gönderen fonksiyonu yazınız.

"""



def sembolleriTemizle(tumKelimeler):
    sembolsuzkelimeler = []
    semboller = "!'@.^#<>+-_{}\",[]-=:;*/’)(&"
    for kelime in tumKelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol,"")
        if(len(kelime)>0):
            sembolsuzkelimeler.append(kelime)
    return sembolsuzkelimeler

def kelimeKaçkereGeçiyor(kelime,dosyaismi):
    with open(dosyaismi,"r") as dosya:
        tümKelimeler = []
        icerik = dosya.read()
        tümKelimeler = icerik.lower().split()
        tümKelimeler = sembolleriTemizle(tümKelimeler)
    sayi = 0
    for i in tümKelimeler:
        if kelime == i:
            sayi+=1
    return sayi
    
def kelime_var_mi(kelime,dosyaismi):
    with open(dosyaismi,"r") as dosya:
        tümKelimeler = []
        icerik = dosya.read()
        tümKelimeler = icerik.lower().split()
        tümKelimeler = sembolleriTemizle(tümKelimeler)
    
    for i in tümKelimeler:
        if kelime == i:
            return 1
    return 0
    
def kelimeninDosyadakiYerleri(kelime,dosyaismi):
    with open(dosyaismi,"r") as dosya:
        tümKelimeler = []
        icerik = dosya.read()
        tümKelimeler = icerik.lower().split()
        tümKelimeler = sembolleriTemizle(tümKelimeler)
        GeçtigiYerler = []
        j = 0
    for i in tümKelimeler:
        j+=1
        if kelime == i:
            GeçtigiYerler.append(j)
    return GeçtigiYerler



kelime = input("lütfen bir kelime giriniz...")

print(kelime_var_mi(kelime,"1.txt"))
print("kelimeden şukadar var :",kelimeKaçkereGeçiyor(kelime,"1.txt"))
print("kelimenin geçtiği yerler(kelimenin listedeki indexi+1)yani kelimenin nerede olduğu:",kelimeninDosyadakiYerleri(kelime,"1.txt"))



















