from ast import If
from itertools import count
import math
import string
from xmlrpc.client import boolean
print("Rumus Dsitribusi Binomial")
print("P(n,x): nCx(p)^x ( Qn)^(n-x) ")
n = int(input("Berapa banyak sampel : "))    
x = int(input("banyak perstiwa yang sukses: ")) 
p = float(input("Banyak Probabilitas sukses: (masukkan 0 jika tidak ada)"))
probSuksesTotal = 0
Qt = bool(int(input("apakah X yang diminta berlanjut? ")))

qn = 1 - p
if p == 0:
    p = x/n
if Qt == True:
    Qy = int(input("jika x berlanjut berlanjut sampai berapa:  "))
    for i in range (x, Qy+1):
        count_result1 = (math.factorial(n))/math.factorial((n - i))/(math.factorial(i)) * (p ** i) * (qn**(n-i))
        probSuksesTotal = probSuksesTotal + count_result1
        print(i,count_result1)
        


else:
    count_result1 = (math.factorial(n))/math.factorial((n - x))/(math.factorial(x)) * (p ** x) * (qn**(n-x))
    probSuksesTotal = count_result1
    
print("Probabilitas sukses total = ", probSuksesTotal)
print(p)
    
        


    



    