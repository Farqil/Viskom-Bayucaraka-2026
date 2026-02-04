import cv2
import numpy as np

# Baca gambar
img = cv2.imread("img/img.jpg")
if img is None:
    print("Gambar tidak ditemukan")
    exit()

# Ubah BGR ke HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Range warna merah (2 range karena merah di 2 ujung Hue)
lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 70, 50])
upper_red2 = np.array([180, 255, 255])

# Buat mask biner dan gabungkan
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = mask1 | mask2

# Cari kontur dari mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Salin gambar untuk digambar bounding box
bbox_img = img.copy()

# Gambar bounding box + teks
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt) # Hitung bounding box
    cv2.rectangle(bbox_img, (x, y), (x + w, y + h), (0, 0, 0), 2) # Gambar kotak
    cv2.putText(bbox_img, "Red", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2) # Tulis label

# Tampilkan hasil
cv2.imshow("Bounding Box", bbox_img)

cv2.waitKey(0)
cv2.destroyAllWindows()