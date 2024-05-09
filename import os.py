import os
import json

# Ana klasör yolu
main_folder_path = r"C:\face1"

# JSON dosyası için boş bir dictionary oluştur
data = {}

# Ana klasördeki her bir alt klasör için
for folder_name in os.listdir(main_folder_path):
    folder_path = os.path.join(main_folder_path, folder_name)
    if os.path.isdir(folder_path):
        # Alt klasördeki dosya isimlerini listele ve sırala
        file_list = sorted(os.listdir(folder_path))
        data[folder_name] = file_list


json_path = 'output.json'
with open(json_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"JSON dosyası {json_path} konumuna başarıyla kaydedildi.")
