import os
from PIL import Image

char_translation_dict = {
    'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u',
    'Ç': 'C', 'Ğ': 'G', 'İ': 'I', 'Ö': 'O', 'Ş': 'S', 'Ü': 'U',
    " ":"_"
}


folder_path =  r"C:\face1"
def changed_name():
    for filename in os.listdir(folder_path):
        
        new_filename = ''.join(char_translation_dict.get(char, char) for char in filename)

        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        os.rename(old_file, new_file)
        
        print(f'Dosya adı "{filename}" olan dosya "{new_filename}" olarak değiştirildi.')

def changed_format():
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".jpeg") or filename.endswith(".webp"):
                file_path = os.path.join(root, filename)  
                with Image.open(file_path) as img:
                    new_file_path = file_path.rsplit('.', 1)[0] + '.jpg'
                    img.convert('RGB').save(new_file_path, 'JPEG')
                    os.remove(file_path) 
                    print(f'{filename} dosyası "{new_file_path}" olarak jpg formatına dönüştürüldü ve orijinal dosya silindi.')

def rename_images():
  
    for root, dirs, files in os.walk(folder_path):
        if root != folder_path:  
            folder_name = os.path.basename(root) 
            sorted_files = sorted([f for f in files if f.endswith(('.jpeg', '.jpg', '.webp', '.png'))])  # Görsel dosyaları sırala
            for index, filename in enumerate(sorted_files, start=1):
                file_path = os.path.join(root, filename)
                new_filename = f"{folder_name}_{index}.jpg"
                new_file_path = os.path.join(root, new_filename)
                os.rename(file_path, new_file_path)  # Dosyanın adını değiştir
                print(f'{filename} dosyası "{new_filename}" olarak yeniden adlandırıldı.')


changed_name()
changed_format()
rename_images()

