import os
import random
import shutil

# Yeni oluşturulan görüntülerin bulunduğu klasör
orijinal_klasor = "images"

# Train ve test klasörlerinin adları
train_klasor = "train"
test_klasor = "test"

# Train ve test klasörlerini oluştur
if not os.path.exists(train_klasor):
    os.makedirs(train_klasor)
if not os.path.exists(test_klasor):
    os.makedirs(test_klasor)

# Orijinal klasördeki dosyaları listele
dosyalar = os.listdir(orijinal_klasor)

# Train ve test klasörlerine dağıtılacak dosyaların listeleri
train_dosyalar = []
test_dosyalar = []

# Dosyaları train ve test olarak ayır
for dosya in dosyalar:
    if dosya.endswith(".png"):
        if random.random() < 0.8:  # %80 train, %20 test olarak ayır
            train_dosyalar.append(dosya)
        else:
            test_dosyalar.append(dosya)

# Train ve test dosyalarını ilgili klasörlere kopyala
for dosya in train_dosyalar:
    kaynak = os.path.join(orijinal_klasor, dosya)
    hedef = os.path.join(train_klasor, dosya)
    shutil.copyfile(kaynak, hedef)

for dosya in test_dosyalar:
    kaynak = os.path.join(orijinal_klasor, dosya)
    hedef = os.path.join(test_klasor, dosya)
    shutil.copyfile(kaynak, hedef)
