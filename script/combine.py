import pandas as pd


# İlk CSV dosyasını yükle
df1 = pd.read_csv('./train3.csv')

# İkinci CSV dosyasını yükle
df2 = pd.read_csv('./train3-3.csv')

# İki veri çerçevesini birleştir
birlesik_df = pd.concat([df1, df2], ignore_index=True)

# Birleştirilmiş veri çerçevesini CSV olarak kaydet
birlesik_df.to_csv('all_dataset.csv', index=False)

print("Dosyalar başarıyla birleştirildi ve 'birlesik_dosya.csv' olarak kaydedildi.")
