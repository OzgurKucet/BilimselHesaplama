# -*- coding: utf-8 -*-
#data = text.decode("iso 8859-15")    
#writer.write(data.encode("UTF-8"))
"""
Created on Sun Mar 22 16:50:00 2020

@author: Ozgur Kucet

tersten okunuşu ile aynı olan kelimeleri test eden bir fonksiyon yazınız.

"""


def terstenOkunusuAyniMi(kelime):
    kelime1 = ""
    for i in range(len(kelime)-1,-1,-1):
        kelime1 = kelime1+kelime[i]
    if kelime1 == kelime:
        return 1
    return 0


with open("1.txt","r") as dosya:
        tümKelimeler = []
        icerik = dosya.read()
        tümKelimeler = icerik.lower().split()

print("girilen txt dosyasındaki tersten okunusu ile aynı olan kelimeler...")

for i in tümKelimeler:
    if terstenOkunusuAyniMi(i) == 1:
        print(i)

        
    
