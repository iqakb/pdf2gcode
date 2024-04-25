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


## Kalibrasi
1. Offset defaultnya adalah x=40mm dan y=17mm. Untuk mengecek apakah sudah cocok, print file gcode `cal_4333_40_17.gcode`
2. Jika belum cocok, jalan skrip `offset.py` dengan syntax berikut
```bash
python3.8 ~/larprak/offset.py -f <namafileinput.gcode> -o <namafileoutput.gcode> -x <offset x dalam milimeter> -y <offset y dalam milimeter>
```
contoh:
```bash
python3.8 ~/larprak/offset.py -f tes.gcode -o tesgeser.gcode -x 12 -y -2.3
```
3. Offset `cal_4333_40_17.gcode` sesuai kebutuhan
4. Cek ulang hasil offset


### Alat lain:
* `convertor.sh` untuk mengonversi pdf banyak halaman ke gcode dengan penggeseran artifisial
* `convertor_s.sh` untuk mengonversi pdf satu halaman ke gcode dengan penggseran artifisial
* `processor.py` untuk mengonversi gcode untuk bisa digunakan pada 3d printer dengan penggeseran artifisial
* `convertor.sh` untuk mengonversi gcode untuk bisa digunakan pada 3d printer tanpa penggeseran artifisial
* `offset.py` untuk menggeser keseluruhan file gcode