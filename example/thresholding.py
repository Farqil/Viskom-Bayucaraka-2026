import cv2
import numpy as np

# Baca gambar
img = cv2.imread("example\img\img.jpg")
if img is None:
    print("Gambar tidak ditemukan")
    exit()

# Konversi dari BGR ke HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Range warna merah (2 range karena merah di 2 ujung Hue)
lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 70, 50])
upper_red2 = np.array([180, 255, 255])

# Buat mask untuk masing-masing range
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

# Gabungkan kedua mask
mask = mask1 | mask2

# Ambil bagian gambar yang berwarna merah saja
result = cv2.bitwise_and(img, img, mask=mask)

# Tampilkan hasil
cv2.imshow("Original", img)
cv2.imshow("Mask", mask)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()