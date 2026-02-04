import cv2

# Baca gambar
image_path = "img/img.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Gambar tidak ditemukan")
    exit()

# Tampilkan gambar
cv2.imshow("Gambar Asli", img)

# Simpan ulang gambar (contoh)
cv2.imwrite("img/output.jpg", img)

# Tunggu sampai ada tombol ditekan
cv2.waitKey(0)
cv2.destroyAllWindows()