
import pandas as pd

# Okunacak CSV dosyasının adını ve hedef dosyanın adını tanımla
input_file = './train.csv'
output_file = 'train1.csv'

# Dosyayı satır satır oku ve eksik sütunları boş değerlerle doldurarak düzelt
with open(input_file, 'r') as f:
    lines = f.readlines()

fixed_lines = []
max_columns = 195

for line in lines:
    # Her satırı virgülle ayırarak sütunları bul
    columns = line.strip().split(',')
    
    # Eğer sütun sayısı 188'den az ise, eksik sütunları boş değerlerle doldur
    if len(columns) < max_columns:
        columns += [''] * (max_columns - len(columns))
    
    # Düzgünleştirilmiş satırı ekleyerek düzeltilmiş veriyi oluştur
    fixed_lines.append(','.join(columns) + '\n')

# Düzgünleştirilmiş veriyi yeni bir CSV dosyasına yaz
with open(output_file, 'w') as f:
    f.writelines(fixed_lines)

# Veriyi Pandas DataFrame'e yükle ve kontrol etmek için gö
