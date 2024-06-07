import pandas as pd

# Dosyanın okunması
df = pd.read_csv("./train2-2.csv", header=None)

# Başlıkların atanması
header_names = ["dish_id", "total_calories", "total_mass", "total_fat", "total_carb"]
num_unnamed_columns = 279 - len(header_names)  # Toplam sütun sayısından belirlenen başlık sayısının çıkarılması

# Diğer sütunların isimlendirilmesi
unnamed_columns = [f"unnamed{i}" for i in range(1, num_unnamed_columns + 1)]
header_names.extend(unnamed_columns)

df.columns = header_names

# Verinin yazdırılması
print(df)

# Dosyanın kaydedilmesi
df.to_csv("train3-3.csv", index=False)
