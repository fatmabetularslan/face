import os
import cv2
from retinaface import RetinaFace
import pandas as pd

# Klasör yolu
base_path = r"C:\face1"

# Tüm alt klasörleri listele
subfolders = [f.path for f in os.scandir(base_path) if f.is_dir()]

# Yüz algılama ve özellik çıkarma
face_details = []

for folder in subfolders:
    for img_file in os.listdir(folder):
        img_path = os.path.join(folder, img_file)
        if img_file.lower().endswith(('png', 'jpg', 'jpeg')):  
            try:
           
                faces = RetinaFace.detect_faces(img_path)
                if isinstance(faces, dict):  
                    for face_key, face_value in faces.items():
                        details = {
                            'image_path': img_path,
                            'face_id': face_key,
                            'facial_area': face_value['facial_area'],
                            'landmarks': face_value['landmarks'],
                            'confidence': face_value['score']
                        }
                        face_details.append(details)
                else:
                    print(f"Yüz algılanamadı: {img_path}")
            except Exception as e:
                print(f"Hata: {e} - {img_path}")


df = pd.DataFrame(face_details)
df.to_csv(r"C:\face1\face_details.csv", index=False)
print("Yüz algılama ve özellik çıkarma işlemi tamamlandı.")
