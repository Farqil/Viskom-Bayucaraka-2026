# Visi Komputer dengan OpenCV

### Apa itu OpenCV?
OpenCV (Open Source Computer Vision Library) adalah library open-source yang digunakan untuk pengolahan citra dan visi komputer. OpenCV menyediakan berbagai fungsi siap pakai untuk:
- Membaca dan menulis gambar atau video
- Memproses citra (filtering, thresholding, segmentasi, transformasi)
- Mendeteksi objek, tepi, kontur, wajah, dan fitur lainnya
- Melakukan analisis bentuk dan ukuran objek pada citra

Secara konsep:
- OpenCV membaca gambar dari file atau kamera.
- Gambar disimpan di memori sebagai array NumPy (matriks piksel).
- Setiap piksel memiliki nilai intensitas (untuk grayscale) atau nilai warna (untuk citra berwarna).
- Fungsi-fungsi OpenCV memanipulasi nilai piksel tersebut untuk menghasilkan citra baru (misalnya hasil thresholding, deteksi kontur, dll).
- Hasil pemrosesan bisa ditampilkan ke layar atau disimpan kembali ke file.
Jadi, OpenCV bekerja dengan cara memproses matriks angka yang merepresentasikan citra.

Sistem Warna dalam OpenCV:
1. BGR (Blue, Green, Red)
Ini adalah format default OpenCV.
Setiap piksel punya 3 nilai: B, G, dan R.
Contoh: (255, 0, 0) berarti biru penuh (bukan merah).

2. Grayscale
Hanya memiliki 1 channel (intensitas cahaya).
Nilai 0 = hitam, 255 = putih.

3. HSV (Hue, Saturation, Value)
Hue: jenis warna (merah, hijau, biru, dll)
Saturation: kejenuhan warna
Value: tingkat kecerahan
HSV sangat berguna untuk deteksi warna, karena lebih stabil terhadap perubahan cahaya dibanding RGB/BGR.

### Instalasi & Setup

### 1. Cek Python
Jalankan di terminal / command prompt:
```bash
$ python --version
```

### 2. Install Library
```bash
$ pip install opencv-python numpy
```

### 1. Membaca Citra

### Tujuan
- Membaca file gambar menggunakan OpenCV  
- Menampilkan gambar ke layar  
- Menyimpan gambar hasil pemrosesan ke file  
- Memahami bahwa citra direpresentasikan sebagai matriks piksel  

### Penjelasan
Gambar dibaca menggunakan fungsi `cv2.imread()` dan disimpan sebagai array NumPy dengan format warna BGR (Blue, Green, Red). Untuk menampilkan gambar digunakan `cv2.imshow()`. Agar window tidak langsung tertutup, digunakan `cv2.waitKey()`, dan `cv2.destroyAllWindows()` untuk menutup semua window yang terbuka. Selain itu, OpenCV juga menyediakan fungsi `cv2.imwrite()` untuk menyimpan citra ke dalam file setelah dibaca atau diproses.

### Fungsi yang digunakan

#### 1. `cv2.imread(path, flags)`
- Fungsi ini digunakan untuk membaca file gambar dari disk.  
- Parameter `path` berisi lokasi file gambar.  
- Parameter `flags` menentukan mode pembacaan (misalnya berwarna, grayscale, atau tanpa perubahan).  
- Hasilnya adalah array NumPy yang berisi nilai piksel gambar.  
- Jika file tidak ditemukan atau path salah, fungsi ini akan mengembalikan `None`.  

#### 2. `cv2.imshow(window_name, image)`
- Fungsi ini digunakan untuk menampilkan gambar ke dalam sebuah window.  
- `window_name` adalah nama window yang akan ditampilkan.  
- `image` adalah array citra hasil pembacaan atau pemrosesan.  
- Window ini tidak akan bertahan lama tanpa `cv2.waitKey()`.  

#### 3. `cv2.waitKey(delay)`
- Fungsi ini menunggu input keyboard selama `delay` milidetik.  
- Jika `delay = 0`, program akan menunggu tanpa batas sampai pengguna menekan tombol.  
- Fungsi ini penting agar window tidak langsung tertutup.  

#### 4. `cv2.destroyAllWindows()`
- Fungsi ini digunakan untuk menutup semua window yang dibuat oleh OpenCV.  
- Biasanya dipanggil setelah selesai menampilkan gambar.  

#### 5. `cv2.imwrite(filename, image)`
- Fungsi ini digunakan untuk menyimpan citra ke dalam file di disk.  
- Parameter `filename` berisi nama dan path file tujuan (misalnya `"output.jpg"`).  
- Parameter `image` adalah array citra yang ingin disimpan.  
- Fungsi ini mengembalikan nilai `True` jika penyimpanan berhasil, dan `False` jika gagal.  
- Fungsi ini berguna untuk menyimpan hasil pemrosesan citra, misalnya setelah dilakukan thresholding, deteksi kontur, atau penambahan bounding box.  

## 2. Thresholding Warna

### Tujuan
- Melakukan segmentasi warna pada citra
- Memisahkan objek berdasarkan rentang warna tertentu
- Menghasilkan citra biner (mask)

### Penjelasan
Citra awal dikonversi dari BGR ke HSV menggunakan `cv2.cvtColor()`. Ruang warna HSV memudahkan pemilihan warna berdasarkan nilai Hue. Setelah itu ditentukan batas bawah dan atas warna yang ingin dideteksi, lalu dibuat mask menggunakan `cv2.inRange()`. Mask ini dapat digunakan untuk mengambil bagian citra tertentu menggunakan `cv2.bitwise_and()`.

### Fungsi yang digunakan

#### 1. `cv2.cvtColor(src, code)`
- Digunakan untuk mengubah ruang warna citra.
- `src` adalah citra input.
- `code` adalah kode konversi warna, misalnya `cv2.COLOR_BGR2HSV`.
- Hasilnya adalah citra baru dalam ruang warna yang berbeda.

#### 2. `cv2.inRange(src, lowerb, upperb)`
- Digunakan untuk melakukan thresholding berdasarkan rentang nilai tertentu.
- `src` adalah citra input (biasanya HSV).
- `lowerb` dan `upperb` adalah batas bawah dan atas warna.
- Output berupa citra biner (mask): piksel dalam rentang akan bernilai 255 (putih), lainnya 0 (hitam).

#### 3. `cv2.bitwise_and(src1, src2, mask)`
- Digunakan untuk menerapkan mask ke citra.
- Operasi AND bitwise akan mempertahankan piksel yang sesuai dengan mask.
- Biasanya `src1` dan `src2` adalah citra yang sama, dan `mask` adalah hasil `inRange()`.

## 3. Contour Detection

### Tujuan
- Mendeteksi batas/bentuk objek pada citra biner
- Mengambil informasi kontur dari hasil thresholding
- Menampilkan kontur pada citra asli

### Penjelasan
Contour dideteksi dari citra biner hasil thresholding. Fungsi `cv2.findContours()` digunakan untuk mencari semua kontur yang ada. Setiap kontur merepresentasikan batas suatu objek dalam bentuk kumpulan titik. Kontur yang ditemukan dapat digambar kembali pada citra menggunakan `cv2.drawContours()`.

### Fungsi yang digunakan

#### 1. `cv2.findContours(image, mode, method)`
- Digunakan untuk mencari kontur pada citra biner.
- `image` adalah citra input (biasanya hasil thresholding).
- `mode` menentukan bagaimana kontur diambil (misalnya semua kontur atau hanya yang luar).
- `method` menentukan metode aproksimasi kontur.
- Output berupa list kontur, di mana setiap kontur adalah kumpulan titik.

#### 2. `cv2.drawContours(image, contours, contourIdx, color, thickness)`
- Digunakan untuk menggambar kontur pada citra.
- `image` adalah citra tempat kontur akan digambar.
- `contours` adalah daftar kontur hasil `findContours()`.
- `contourIdx` menentukan kontur mana yang digambar (atau -1 untuk semua).
- `color` menentukan warna garis kontur.
- `thickness` menentukan ketebalan garis.

## 4. Bounding Box

### Tujuan
- Menentukan posisi dan ukuran objek yang terdeteksi
- Memberi kotak pembatas (bounding box) pada objek
- Menandai objek pada citra hasil deteksi

### Penjelasan
Dari kontur yang telah diperoleh, dapat dihitung kotak pembatas menggunakan `cv2.boundingRect()`. Fungsi ini menghasilkan koordinat (x, y, w, h) yang merepresentasikan posisi dan ukuran kotak. Kotak tersebut kemudian digambar pada citra menggunakan `cv2.rectangle()`.

### Fungsi yang digunakan

#### 1. `cv2.boundingRect(points)`
- Digunakan untuk menghitung persegi panjang terkecil yang membungkus suatu kontur.
- `points` adalah satu kontur (kumpulan titik).
- Output berupa `(x, y, w, h)`:
  - `x, y` = koordinat pojok kiri atas
  - `w, h` = lebar dan tinggi kotak

#### 2. `cv2.rectangle(img, pt1, pt2, color, thickness)`
- Digunakan untuk menggambar persegi panjang pada citra.
- `img` adalah citra tujuan.
- `pt1` adalah titik kiri atas (x, y).
- `pt2` adalah titik kanan bawah (x+w, y+h).
- `color` menentukan warna garis kotak.
- `thickness` menentukan ketebalan garis.
