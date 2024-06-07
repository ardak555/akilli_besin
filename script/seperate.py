import os
import shutil
import random

# Ana klasör yolu
ana_klasor_yolu = "image"

# Train ve test klasörlerinin yolları
train_klasor_yolu = "train"
test_klasor_yolu = "test"

# Eğer train ve test klasörleri yoksa oluştur
if not os.path.exists(train_klasor_yolu):
    os.makedirs(train_klasor_yolu)
if not os.path.exists(test_klasor_yolu):
    os.makedirs(test_klasor_yolu)

# Ana klasörün içindeki klasörleri liste olarak al
klasorler = os.listdir(ana_klasor_yolu)

# Her klasörü rastgele train veya test klasörüne kopyala
for klasor in klasorler:
    klasor_yolu = os.path.join(ana_klasor_yolu, klasor)
    if os.path.isdir(klasor_yolu):
        dosyalar = os.listdir(klasor_yolu)
        random.shuffle(dosyalar)  # Dosyaları karıştır
        # Train ve test klasörlerine kopyala
        for dosya in dosyalar:
            dosya_yolu = os.path.join(klasor_yolu, dosya)
            if os.path.isfile(dosya_yolu):
                if random.random() < 0.8:  # %80 train, %20 test olarak ayır
                    shutil.copy(dosya_yolu, os.path.join(train_klasor_yolu, klasor))
                else:
                    shutil.copy(dosya_yolu, os.path.join(test_klasor_yolu, klasor))
