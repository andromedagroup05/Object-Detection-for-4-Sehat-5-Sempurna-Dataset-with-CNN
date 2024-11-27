# import cv2
# import numpy as np
# from tensorflow.keras.models import load_model

# # Muat model yang sudah dilatih
# model_path = 'object_detection_model.h5'  # Ubah sesuai path model Anda
# model = load_model(model_path)

# # Label kelas makanan dan minuman (pastikan urutannya sesuai dengan model Anda)
# class_labels = ['karbohidrat', 'protein', 'buah', 'sayur', 'minuman']

# def preprocess_frame(frame):
#     """Preprocessing frame untuk prediksi"""
#     frame_resized = cv2.resize(frame, (150, 150))
#     frame_resized = frame_resized / 255.0
#     img_array = np.expand_dims(frame_resized, axis=0)
#     return img_array

# # Mengakses kamera
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame = cv2.flip(frame, 1)
#     h, w, _ = frame.shape

#     # Ubah frame menjadi RGB
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Convert frame to grayscale and apply GaussianBlur
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)

#     # Thresholding untuk mendeteksi objek makanan
#     _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)
#     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     for contour in contours:
#         if cv2.contourArea(contour) > 500:  # Filter area kecil
#             # Dapatkan bounding box dari kontur
#             x, y, w, h = cv2.boundingRect(contour)

#             # Ekstraksi area makanan/minuman
#             food_img = frame[y:y+h, x:x+w]

#             if food_img.size != 0:
#                 # Preprocess gambar untuk prediksi
#                 img_array = preprocess_frame(food_img)
#                 predictions = model.predict(img_array)
#                 predicted_index = np.argmax(predictions[0])

#                 # Multi-label classification berdasarkan threshold tertentu
#                 threshold = 0.5
#                 labels = []
#                 for idx, confidence in enumerate(predictions[0]):
#                     if confidence > threshold:
#                         labels.append(f"{class_labels[idx]} ({confidence:.2f})")
                
#                 # Jika ada label yang terdeteksi, tampilkan di bounding box
#                 if labels:
#                     label_text = ', '.join(labels)
#                     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#                     cv2.putText(frame, label_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

#     # Tampilkan frame
#     cv2.imshow("Food & Drink Detection", frame)

#     # Tekan 'q' untuk keluar
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Muat model yang sudah dilatih
model_path = 'object_detection_model.h5'  # Ubah sesuai path model Anda
model = load_model(model_path)

# Label kelas makanan dan minuman (pastikan urutannya sesuai dengan model Anda)
class_labels = ['karbohidrat', 'protein', 'buah', 'sayur', 'minuman']

def preprocess_frame(frame):
    frame_resized = cv2.resize(frame, (150, 150))
    frame_resized = frame_resized / 255.0
    img_array = np.expand_dims(frame_resized, axis=0)
    return img_array

# Fungsi untuk menggambar bounding box dengan rounded corners
def draw_rounded_rectangle(img, top_left, bottom_right, color, thickness=2, radius=10):
    x1, y1 = top_left
    x2, y2 = bottom_right

    # Gambarkan 4 garis lurus
    cv2.line(img, (x1 + radius, y1), (x2 - radius, y1), color, thickness)
    cv2.line(img, (x1 + radius, y2), (x2 - radius, y2), color, thickness)
    cv2.line(img, (x1, y1 + radius), (x1, y2 - radius), color, thickness)
    cv2.line(img, (x2, y1 + radius), (x2, y2 - radius), color, thickness)

    # Gambarkan 4 sudut dengan bentuk lingkaran
    cv2.ellipse(img, (x1 + radius, y1 + radius), (radius, radius), 180, 0, 90, color, thickness)
    cv2.ellipse(img, (x2 - radius, y1 + radius), (radius, radius), 270, 0, 90, color, thickness)
    cv2.ellipse(img, (x1 + radius, y2 - radius), (radius, radius), 90, 0, 90, color, thickness)
    cv2.ellipse(img, (x2 - radius, y2 - radius), (radius, radius), 0, 0, 90, color, thickness)

# Mengakses kamera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Thresholding untuk mendeteksi objek makanan
    _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Filter area kecil
            x, y, w, h = cv2.boundingRect(contour)
            food_img = frame[y:y+h, x:x+w]

            if food_img.size != 0:
                img_array = preprocess_frame(food_img)
                predictions = model.predict(img_array)
                predicted_index = np.argmax(predictions[0])

                threshold = 0.5
                labels = []
                for idx, confidence in enumerate(predictions[0]):
                    if confidence > threshold:
                        labels.append(f"{class_labels[idx]} ({confidence:.2f})")
                
                if labels:
                    label_text = ', '.join(labels)

                    # Warna Bounding Box (Biru)
                    color = (255, 0, 0)
                    draw_rounded_rectangle(frame, (x, y), (x+w, y+h), color, thickness=3, radius=15)

                    # Menampilkan teks di atas bounding box
                    cv2.putText(frame, label_text, (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    cv2.imshow("Food & Drink Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
