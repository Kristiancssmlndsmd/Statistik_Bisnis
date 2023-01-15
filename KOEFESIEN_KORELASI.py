import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file_1 = 'book123.xlsx'


df_first_shift = pd.read_excel(excel_file_1, sheet_name='Statistik_biasa')

print(df_first_shift)
print(df_first_shift['X^2'])
#
#
#
print("DIKETAHUI: ")
#Mencari nilai sigma_X
sigma_X= df_first_shift['X'].sum()
print("sigma_x =", sigma_X)

#Mencari nilai n 
n =df_first_shift['X^2'].value_counts().sum(axis=0)
print("n =", n)

#Mencari sigma_Y
sigma_Y= df_first_shift['Y'].sum()
print('sigma_Y', sigma_Y)

#Mencari sigma_XY
sigma_XY = df_first_shift['XY'].sum()
print('sigma_XY', sigma_XY)

#Mencari sigma_X^2
sigma_X_kuadrat = df_first_shift['X^2'].sum()
print("sigma_X_kuadrat", sigma_X_kuadrat)

#Mencari sigma_Y^2
sigma_Y_kuadrat = df_first_shift['Y^2'].sum()
print("sigma_Y_kuadrat",sigma_Y_kuadrat)

#RUMUS
count_result1 = ((n) * sigma_XY) - ( sigma_X * sigma_Y)
count_result2 = ((((n)*sigma_X_kuadrat) -(sigma_X)**2)*(((n)*sigma_Y_kuadrat)-(sigma_Y)**2))**0.5

#Mencari Koefesien Relasi
def Koefesien_korelasi():
     print(count_result1/count_result2)
     
print("Koefesien Korelasi: ")
Koefesien_korelasi()
print("(",n,"*",sigma_XY,")","-",sigma_X,"*",sigma_Y)
print(n*sigma_X_kuadrat)
print(count_result1)
print(count_result2)
    
    
    



