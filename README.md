# larprak
*Pengelar Laporan Praktikum*

## Langkah Penggunaan
1. Buat dokumen dalam format svg dengan data vektor semua. Bisa dilakukan dengan Adobe Illustrator atau mengonversi file pdfmu ke svg
2. Konversi svg dokumen itu ke gcode menggunakan website: https://sameer.github.io/svg2gcode/
3. Proses ulang gcode dokumenmu dengan `processor.py`. Pastikan gcodemu tidak melebihi 10000x10000mm
4. Tinjau ulang hasil gcode yang terproses dengan https://zupfe.velor.ca/. Jika ada keganjalan, berarti, pada kode `processor.py`, ada yang salah.
4. Kirim gcode dokumen ke 3D printer
5. Kalibrasi penamu sehingga pena menyentuh bed 3d printer atau kertas saat z=5mm. Gunakan komunikasi serial
6. Setting sehingga z=10mm
7. Print gcode dokumenmu
