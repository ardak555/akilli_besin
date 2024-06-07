import os
import shutil

# Kaydedilecek yeni klasörün adı
yeni_klasor_adı = "images"

# Eğer yeni_klasor adında bir klasör yoksa oluştur
if not os.path.exists(yeni_klasor_adı):
    os.makedirs(yeni_klasor_adı)

# image klasöründeki klasörleri listele
image_klasoru = "image"
klasorler = os.listdir(image_klasoru)

# Her klasör için işlem yap
for klasor in klasorler:
    klasor_yolu = os.path.join(image_klasoru, klasor)
    # Eğer klasor bir klasör değilse geç
    if not os.path.isdir(klasor_yolu):
        continue
    
    # Klasörün içindeki dosyaları listele
    dosyalar = os.listdir(klasor_yolu)
    
    # Her dosya için işlem yap
    for dosya in dosyalar:
        # Dosyanın adı rgb.png ile bitiyorsa
        if dosya.endswith("rgb.png"):
            # Yeni dosyanın adı ve yolu
            yeni_dosya_adi = klasor + ".png"
            yeni_dosya_yolu = os.path.join(yeni_klasor_adı, yeni_dosya_adi)
            # Dosyayı yeni klasöre kopyala
            shutil.copyfile(os.path.join(klasor_yolu, dosya), yeni_dosya_yolu)
