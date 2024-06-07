import os
import shutil
import random

# Orjinal veri klasörü
data_folder = "image"

# Train ve test klasörlerinin oluşturulması
train_folder = "train"
test_folder = "test"

os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Veri klasöründeki alt klasörlerin listelenmesi
subfolders = [f.path for f in os.scandir(data_folder) if f.is_dir()]

# Her bir alt klasördeki görüntü sayısının belirlenmesi
# Burada her bir alt klasördeki görüntülerin yüzde 80'i train, yüzde 20'si test olarak ayrılıyor
for subfolder in subfolders:
    # Alt klasör adını al
    subfolder_name = os.path.basename(subfolder)
    
    # Alt klasördeki görüntülerin listelenmesi
    images = [f.name for f in os.scandir(subfolder) if f.is_file()]
    random.shuffle(images)
    num_train_images = int(0.8 * len(images))
    
    # Train ve test görüntülerinin kopyalanması
    for image in images[:num_train_images]:
        shutil.copy(os.path.join(subfolder, image), os.path.join(train_folder, subfolder_name))
    for image in images[num_train_images:]:
        shutil.copy(os.path.join(subfolder, image), os.path.join(test_folder, subfolder_name))

print("Veri ayrımı tamamlandı.")
