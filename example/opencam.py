import cv2

# Buka webcam (0 = kamera default)
cam = cv2.VideoCapture(0)

# Cek apakah kamera berhasil dibuka
if not cam.isOpened():
    print("Webcam tidak bisa dibuka")
    exit()

while True:
    # Baca satu frame dari webcam
    ret, frame = cam.read()
    if not ret:
        print("Gagal membaca frame dari webcam")
        break

    # Tampilkan frame
    cv2.imshow("Webcam", frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()