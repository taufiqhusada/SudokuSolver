# Sudoku Solver
Author: Taufiq Husada Daryanto <br/>
NIM: 13518058

## How to run the program
A. Install the required library
1. Pillow `pip install Pillow`
2. pytesseract (if in windows)
- Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki
- Put the installation on "bin/Tesseract-OCR"

B. Run the program
1. Go to src
2. type in terminal `python main.py`
3. Ikuti arahan dari program
- Masukkan tipe inputan (image/text), masukkan pilihan angkanya saja
- Masukkan nama file input
- Hasil output dapat dilihat di terminal dan external file di folder result

## Strategi pencarian solusi
Strategi yang digunakan adalah backtracking. Proses secara umumnya adalah program mencari cell yang kosong, kemudian mencoba angka dari 1-9 yang valid di cell tersebut, kemudian lanjut terus ke cell berikutnya. Jika di suatu cell ternyata tidak ada angka yang valid, maka program akan backtrack. Program baru berakhir jika semua cell sudah terassign angka.
<br/>
kompleksitas waktu: O(9^(n*n)) <br/>
n adalah jumlah baris/kolom nya
<br/>
Alasan penggunaan algoritma backtracking:
- waktu yang dibutuhkan program lebih singkat dibandingkan brute force, karena walaupun kompleksitas watkunya sama, namun dengan dilakukannya pruning maka jelas program lebih cepat
- implementasi algoritmanya terbilang cukup intuitif dan cukup menggambarkan metode yang dilakukan oleh orang asli ketika bermain sudoku

## Pengerjaan bonus
Berikut adalah library yang digunakan
1. Pillow: untuk mengecrop image
2. Tesseract: untuk mengconvert image angka menjadi angka beneran. Kelebihannya: penggunaannya simpel dan tinggal pake aja. Kekurangannya: ga bisa langsung `pip install pytesseract` doang, tapi juga perlu donlod binarynya

## Referensi
1. https://www.geeksforgeeks.org/sudoku-backtracking-7/
2. https://pillow.readthedocs.io/en/stable/reference/Image.html
3. https://github.com/UB-Mannheim/tesseract/wiki
4. https://stackoverflow.com/questions/50951955 pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i

