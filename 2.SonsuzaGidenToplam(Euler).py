def fak(a):
    faktoriyel = 1
    for i in range(1,a+1):
        faktoriyel*=i
    return faktoriyel

n,e,e1 = 0,1,0
while (e!=e1):#python virgülden sonraki 16 basamağı aldığı için sonsuza kadar dönmez...
    e = e1
    e1 += 1/fak(n)
    n+=1
#
#AlttakiFonksiyonuBenYazdım:
#
def euler():
    from math import factorial
    euler = float(2)
    i=2
    while(i<20):
        euler += 1/fak(i)
        i+=1
    return euler



print(e)
print(euler())



