#pi sayisinin ilk 5 basamaðýný hesaplamak
#4(1- 1/3 + 1/5 -1/7 + 1/9 - 1/11.....)
#Bu yöntemle pi sayýsýný hesaplamak çok zor...

k=0
pi = 0
a = 0
from decimal import Decimal
while(True):
    a = pi
    pi += Decimal(4*((pow(-1,k))/(2*k+1)))
    pi = round(pi,5)
    k+=1
    if a == pi:
        break

print(pi)
