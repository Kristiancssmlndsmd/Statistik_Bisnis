#Peramalan Permintaan Part 2 (Trend Linear/Least Square)
import pandas as pd
data = pd.read_excel("Data_Genap.xlsx")

#Cek apakah jumlah data ganjil atau genap
row_count = len(data.index)
middle_index_ganjil = 0
middle_index_genap1 = 0
middle_index_genap2 = 0
isGenap = True
if(row_count % 2 == 0):
  middle_index_genap1 = row_count/2
  middle_index_genap2 = middle_index_genap1 - 1
  middle_index_genap1 = int(middle_index_genap1)
  middle_index_genap2 = int(middle_index_genap2)
  isGenap = True
elif(row_count % 2 != 0):
  middle_index_ganjil = (row_count - 1)/2
  middle_index_ganjil = int(middle_index_ganjil)
  isGenap = False

#Membuat column baru
data['x'] = ""
data['xy'] = ""
data['x^2'] = ""


#Memasukkan data ke column X
if(isGenap == True):
  data.loc[middle_index_genap1, 'x'] = 1
  data.loc[middle_index_genap2, 'x'] = -1
  masukan = 3
  for index in range(middle_index_genap1+1, row_count):
    data.loc[index, 'x'] = masukan
    masukan = masukan + 2
  masukan = -3
  for index in range(middle_index_genap2-1, -1, -1):
    data.loc[index, 'x'] = masukan
    masukan = masukan + -2

elif(isGenap == False):
  data.loc[middle_index_ganjil, 'x'] = 0
  masukan = 1
  for index in range(middle_index_ganjil+1, row_count):
    data.loc[index, 'x'] = masukan
    masukan = masukan + 1
  masukan = -1
  for index in range(middle_index_ganjil-1, -1, -1):
    data.loc[index, 'x'] = masukan
    masukan = masukan + -1

#Memasukkan data ke column xy
for index in range(0, row_count):
  data.loc[index, 'xy'] = data.loc[index, 'x'] * data.loc[index, 'Penjualan']

#Memasukkan data ke column x^2
for index in range (0, row_count):
  data.loc[index, 'x^2'] = data.loc[index, 'x'] **2

#Memasukkan jumlah Penjualan, xy dan x^2
jml_penjualan = 0
jml_xy = 0
jml_x_pangkat = 0
for index in range (0, row_count):
  jml_penjualan = jml_penjualan + data.loc[index, 'Penjualan']
  jml_xy = jml_xy + data.loc[index, 'xy']
  jml_x_pangkat = jml_x_pangkat + data.loc[index, 'x^2']
idx_jual = row_count
data.loc[idx_jual, 'Tahun'] = "Total = "
data.loc[idx_jual, 'Penjualan'] = jml_penjualan
data.loc[idx_jual, 'xy'] = jml_xy
data.loc[idx_jual, 'x^2'] = jml_x_pangkat
data.loc[idx_jual, 'x'] = 0

a = data['Penjualan'].loc[data.index[row_count]]
a = a / (row_count)

#Mencari nilai b
b = data['xy'].loc[data.index[row_count]]
b = b / data['x^2'].loc[data.index[row_count]]

idx_last = row_count - 1
if(isGenap == True):
  x = data['x'].loc[data.index[idx_last]]
  x = x + 2
elif(isGenap == False):
  x = data['x'].loc[data.index[idx_last]]
  x = x + 1
print(data['xy'])
print(data['x'])
goblok = int(input("masukan tahunya berapa? "))
y = a + (b * goblok)

print("Nilai a = ", a)
print("Nilai b = " , b)
print("Nilai x = " , x)
print("Nilai b * x = ", b * x)
print("Nilai y = " , y)
