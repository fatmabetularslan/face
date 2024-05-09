import os
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
from retinaface import RetinaFace

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


img_path = r"C:\face1\emma_watson\emma_watson_1.jpg"
db_path = r"C:\face1"


result = DeepFace.verify(img1_path=img_path, img2_path=r"C:\face1\emma_watson\emma_watson_2.jpg")
print(result)


try:
    results_list = DeepFace.find(img_path=img_path, db_path=db_path, model_name='VGG-Face', distance_metric='cosine')
    if results_list:
        results = results_list[0]
        if not results.empty:
            print("Eşleşme bulundu! İşte detaylar:")
            print(results[['identity', 'distance']])
        else:
            print("Eşleşme bulunamadı.")
except Exception as e:
    print("Bir hata oluştu:", e)

try:
    resp = RetinaFace.detect_faces(img_path)
    print(resp)
except Exception as e:
    print("RetinaFace.detect_faces hatası:", e)

try:
    faces = RetinaFace.extract_faces(img_path=img_path, align=True)
    for face in faces:
        plt.imshow(face)
        plt.show()
except Exception as e:
    print("RetinaFace.extract_faces hatası:", e)

try:
    obj = DeepFace.verify(img_path, r"C:\face1\emma_watson\emma_watson_2.jpg", model_name='ArcFace', detector_backend='retinaface')
    print(obj["verified"])
except Exception as e:
    print("DeepFace.verify hatası:", e)
