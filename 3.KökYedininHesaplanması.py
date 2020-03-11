#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Kök yediyi 8 basamak hassasiyet ile hesaplayın...

while(True):
    sayi = int(input("Kökünü Hesaplamak istediğiniz bir sayiyi giriniz"))

    if sayi==-1:
        break

    büyük = 0
    while(büyük*büyük<sayi):
        büyük+=1
    küçük = büyük-1
    x = -1
    while(True):
        a = (büyük+küçük)/2
        if a*a > sayi:
            büyük = a
        else:
            küçük = a
        if(a == x):
            break
        x = a
    print(büyük)




