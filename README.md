# larprak
*Pengelar Laporan Praktikum*

## Prasyarat
1. Pasang environment Rust
2. Pasang environment Python
3. Pasang cpp-poppler
4. Pasang ghostscript

## Langkah Pemasangan
1. Clone repositori ini
2. Install cargo svg2gcode dengan menjalankan `cargo install --path cli/`

## Langkah Penggunaan
1. Proses file pdfmu dengan `./convertor.sh <filepdfmu>`. Pastikan pdfmu tidak melebihi 10000x10000mm
2. Tinjau ulang hasil gcode yang terproses dengan https://zupfe.velor.ca/. Jika ada keganjalan, berarti, pada kode `processor.py`, ada yang salah.
3. Kirim gcode dokumen ke 3D printer
4. Kalibrasi penamu sehingga pena menyentuh bed 3d printer atau kertas saat z=5mm. Gunakan komunikasi serial atau menu 3D printer.
5. Setting sehingga z=10mm
6. Print gcode dokumenmu