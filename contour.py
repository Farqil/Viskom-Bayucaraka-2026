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

# Gambar kontur ke salinan gambar
contour_img = img.copy()
cv2.drawContours(contour_img, contours, -1, (0, 0, 0), 2)

# Tampilkan hasil
cv2.imshow("Contour", contour_img)

cv2.waitKey(0)
cv2.destroyAllWindows()