# 🐟 Baso Plembang (Palembangnese Esoteric Transpiler)

[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()
[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)]()

> "Ngapo nak pening palak belajar koding kalu pacak pake baso dewek?"

**Baso Plembang** adalah _esoteric programming language_ (esolang) berorientasi _transpiler_ yang dibangun di atas ekosistem bahasa pemrograman Python. Bahasa ini dirancang khusus dengan mengadopsi struktur sintaks, operasi logika, dan kosakata lokal dari bahasa daerah Palembang, Sumatra Selatan.

Proyek ini dikembangkan sebagai portofolio teknis untuk mendemonstrasikan pemahaman mengenai arsitektur _compiler/transpiler_ tingkat dasar, sekaligus menjadi media edukasi. Tujuannya adalah untuk menurunkan batas masuk (_barrier to entry_) bagi masyarakat awam yang ingin mempelajari algoritma dan logika komputasi dengan pendekatan yang lebih merakyat dan kontekstual.

---

## 📑 Daftar Isi

1. [Latar Belakang dan Filosofi](#1-latar-belakang-dan-filosofi)
2. [Arsitektur Teknis Sistem](#2-arsitektur-teknis-sistem)
3. [Fitur Unggulan](#3-fitur-unggulan)
4. [Kamus Kosakata Sintaks (Cheat Sheet)](#4-kamus-kosakata-sintaks-cheat-sheet)
5. [Panduan Pengguna (Instalasi & Penggunaan)](#5-panduan-pengguna-instalasi--penggunaan)
6. [Panduan Developer (Kloning & Build)](#6-panduan-developer-kloning--build)
7. [Contoh Program Lanjutan](#7-contoh-program-lanjutan)
8. [Troubleshooting dan FAQ](#8-troubleshooting-dan-faq)
9. [Roadmap Pengembangan](#9-roadmap-pengembangan)
10. [Lisensi](#10-lisensi)

---

## 1. Latar Belakang dan Filosofi

Banyak pemula yang merasa terintimidasi saat pertama kali belajar pemrograman karena dihadapkan pada dua dinding besar sekaligus: **logika komputasi** dan **kosakata teknis berbahasa Inggris**. 

Baso Plembang hadir sebagai jembatan. Dengan menggunakan kosakata sehari-hari yang akrab di telinga masyarakat Sumatra Selatan, pengguna dapat memusatkan seluruh energi kognitif mereka untuk murni memahami logika, alur percabangan (*branching*), dan perulangan (*looping*).

---

## 2. Arsitektur Teknis Sistem

Secara fundamental, Baso Plembang beroperasi sebagai _Source-to-Source Compiler_ (Transpiler). Sistem ini tidak menginterpretasikan kode biner dari awal, melainkan menunggangi ketangguhan _engine_ Python melalui alur eksekusi berikut:

- **Lexical Analysis (Tokenizer)**: Mesin akan membaca file berekstensi `.plg` dari pengguna baris demi baris, memecah string menjadi token yang dapat dikenali.
- **Syntax Mapping**: Memanfaatkan ekspresi reguler (Regex) tingkat lanjut, kata kunci khas Palembang dipetakan secara presisi dan diterjemahkan kembali ke dalam tata bahasa Python standar.
- **On-the-fly Execution**: Transpiler akan langsung mengeksekusi hasil terjemahan di memori (_runtime_) menggunakan fungsi bawaan sistem tanpa meninggalkan file sampah (_temporary files_) di direktori pengguna, menjaga ruang kerja tetap rapi.

---

## 3. Fitur Unggulan

- **Native Python Indentation**: Mengadopsi 100% aturan _indentation_ (spasi/tab) Python. Ini memaksa pengguna untuk terbiasa menulis blok kode yang rapi dan terstruktur sejak hari pertama belajar koding.
- **Dedicated IDE Extension**: Dilengkapi ekstensi Visual Studio Code mandiri (`.vsix`) yang menghadirkan fitur pewarnaan sintaks (_Syntax Highlighting_), sehingga kode tidak terlihat sebagai teks mati.
- **Zero-Setup Standalone Executable**: Dibungkus menjadi _binary executable_ (`.exe`). Pengguna tidak perlu dipusingkan dengan pengaturan _environment_ variabel Python atau instalasi pustaka eksternal.

---

## 4. Kamus Kosakata Sintaks (Cheat Sheet)

Pemetaan kata kunci dirancang agar sesederhana mungkin tanpa menghilangkan esensi pemrograman struktural.

| Kategori Logika | Logika Python Standar | Sintaks Baso Plembang | Keterangan / Fungsi |
| :--- | :--- | :--- | :--- |
| **I/O** | `print(...)` | `toleske(...)` | Mencetak teks atau output variabel ke layar terminal. |
| **I/O** | `input(...)` | `masukke(...)` | Menahan eksekusi program untuk meminta masukan pengguna. |
| **Tipe Data** | `int(...)` | `angko(...)` | Melakukan _casting_ tipe data _string_ menjadi bilangan bulat. |
| **Kondisional** | `if ... :` | `kalu ... :` | Pintu gerbang utama untuk percabangan logika. |
| **Kondisional** | `elif ... :` | `kalu_bae ... :` | Kondisi alternatif bersyarat (opsional). |
| **Kondisional** | `else:` | `daknyo:` | Percabangan penutup (nilai bawaan jika logika atas salah). |
| **Boolean** | `True` | `iyo` | Nilai kebenaran logika mutlak (1). |
| **Boolean** | `False` | `dak` | Nilai kesalahan logika mutlak (0). |
| **Fungsional** | `def ... :` | `fungsi ... :` | Mendeklarasikan blok instruksi algoritma (fungsi). |
| **Fungsional** | `return` | `balekke` | Mengembalikan nilai hasil proses dari dalam sebuah fungsi. |
| **Perulangan** | `for x in range(y):` | `tiap x didalem urutan(y):`| Perulangan iterasif dengan batas rentang indeks matematis. |

---

## 5. Panduan Pengguna (Instalasi & Penggunaan)

Untuk pengguna (*end-user*) dan ingin mencoba menjalankan program menggunakan Baso Plembang ini, tinggal ikuti petunjuk dari nol di bawah ini:

### Langkah A: Pasang "Baju Warna-Warni" (Instalasi Ekstensi VS Code)
Langkah pertama ini wajib dilakukan supaya teks kodingan nanti ada warnanya dan jauh lebih gampang dibaca.

1. Kunjungi tab **Releases** di halaman GitHub ini (biasanya ada di panel sebelah kanan layar dekstop).
2. Cari dan unduh (*download*) file yang bernama **`baso-plembang-syntax-1.0.0.vsix`**.
3. Buka aplikasi **Visual Studio Code (VS Code)** di dekstop.
4. Di deretan menu sebelah kiri layar, klik menu **Extensions** (cari ikon bentuk kotak-kotak kubus). Kalau mau jalur cepat, tekan saja tombol `Ctrl + Shift + X` bersamaan di *keyboard*.
5. Coba perhatikan di pojok kanan atas menu Extensions yang baru terbuka tadi, ada ikon **titik tiga (...)**. Klik ikon tersebut.
6. Lalu muncul daftar pilihan (*dropdown*), pilih yang bertuliskan **"Install from VSIX..."**.
7. Akan muncul jendela kecil untuk mencari file. Cari dan pilih file ekstensi `.vsix` yang baru saja diunduh di langkah ke-2 tadi. 
8. Klik *Install* dan tunggu sebentar sampai muncul notifikasi sukses di pojok kanan bawah layar.

### Langkah B: Mulai Menulis dan Jalankan Program
Sekarang "baju"-nya sudah siap, saatnya kita tes mesinnya.

1. Kembali lagi ke tab **Releases** di GitHub tadi. Kali ini, unduh file eksekutor utamanya yang bernama **`plembang.exe`**.
2. Buat satu folder khusus di komputer (bebas di mana saja) untuk proyek ini, lalu letakkan/pindahkan file `plembang.exe` tadi **langsung ke dalam folder** tersebut.
3. Buka lagi VS Code. Buat file baru (*New File*), lalu simpan dengan nama **`namafilekamu.plg`** di dalam folder yang sama dengan letak `plembang.exe` tadi. (Penting: belakangnya harus `.plg` ya!).
4. Silakan tulis program atau kodingan pertamamu di dalam file itu. 
5. **Perhatian:** Lirik ke bawah layar VS Code. Pastikan indikator bahasanya sudah bertuliskan **"Baso Plembang"**. Kalau belum, klik tulisan di situ dan ketik manual "Baso Plembang".
6. Jangan lupa disimpan! Tekan `Ctrl + S` di *keyboard*.
7. Sekarang kita buka kotak Terminal di dalam VS Code. Caranya mudah, tekan aja tombol `Ctrl + \`` (tombol *backtick*, biasanya letaknya di sebelah kiri angka 1).
8. Di kotak terminal hitam yang muncul di bawah layar, ketik ini untuk menjalankan programmu:
   ```bash
   .\plembang.exe namafilekamu.plg
   ```
9. Tekan **Enter**, dan program Baso Plembang buatanmu akan langsung jalan di layar.
    
---

## 6. Panduan Developer (Kloning & Build)

Bagi pengembang yang ingin memodifikasi logika Regex transpiler atau melakukan *tweak* pada warna tema ekstensi.

### A. Struktur Dasar
Lakukan kloning repositori ini ke dalam sistem lokal Anda:

```bash
git clone [https://github.com/kiranaao/baso-plembang.git](https://github.com/kiranaao/baso-plembang.git)
cd baso-plembang
```

- Folder plembang/: Jantung pemrosesan program. Modul Python pengurai teks ada di sini.
- Folder vscode-Extension/: Segala konfigurasi JSON untuk VS Code, termasuk syntaxes/baso-plembang.tmLanguage.json tempat definisi Regex pewarnaan sintaks berada.

### B. Membungkus Ulang Ekstensi (.vsix)

Jika Anda mengedit tata bahasa JSON, Anda harus mem-build ulang paketnya:

```bash
cd vscode-Extension
npm install -g @vscode/vsce
vsce package
```

Proses ini membutuhkan instalasi NodeJS di komputer Anda.

### C. Membungkus Ulang Transpiler (.exe)

Jika backend Python dimodifikasi, konversi kembali menjadi executable menggunakan modul PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile main.py --name plembang
```

---

## 7. Contoh Program Lanjutan

Baso Plembang bukan sekadar mainan untuk mencetak teks sapaan. Bahasa ini mendukung kalkulasi aritmetika yang cukup kompleks.
Berikut adalah contoh skrip pembuktian sifat aljabar: Membuktikan bahwa n^3 - n selalu habis dibagi oleh angka 6 untuk semua bilangan bulat berturut-turut.

``` python
toleske("=== Pembuktian Matematis Baso Plembang ===")
toleske("Ngebuktike rumus: (n^3 - n) selalu abis asak dibagi 6\n")

fungsi cek_rumus(n):
    hasil = (n * n * n) - n
    
    kalu hasil % 6 == 0:
        balekke "Terbukti! Habis dibagi 6."
    daknyo:
        balekke "Dak terbukti, ado error logis."

angka_uji = masukke("Payo masukke angko tes (n): ")
n_bulat = angko(angka_uji)

jawaban = cek_rumus(n_bulat)
toleske("\nHasil kalkulasi kau: ", jawaban)
toleske("Kelar lur, program sukses dijalan ke!")
```

---

## 8. Troubleshooting dan FAQ

Berikut adalah beberapa kendala yang paling sering ditemui beserta solusi praktisnya:

**Q: Kenapa saat install VSIX ada peringatan "LICENSE.md not found"?**  
A: Peringatan dari modul `vsce` ini sangat aman untuk diabaikan. Ketik `y` pada terminal saat pembungkusan, dan fitur ekstensi tetap akan berjalan 100% normal.

**Q: Tulisan di pojok kanan bawah VS Code masih "Plain Text", kode saya tidak berwarna?**  
A: Klik tulisan "Plain Text" tersebut. Akan muncul kotak pencarian *dropdown* di bagian atas layar, lalu ketik dan pilih "Baso Plembang" secara manual untuk memaksa VS Code mengenali file tersebut.

**Q: Terminal memunculkan error "is not recognized as an internal or external command"?**  
A: Pastikan Anda menjalankan perintah eksekusi dari dalam folder yang sama persis dengan tempat file `plembang.exe` berada. Selain itu, pastikan Anda menggunakan prefix `.\` (contoh: `.\plembang.exe namafile.plg`) pada PowerShell Windows.

**Q: Program langsung tertutup (force close) setelah dijalankan tanpa menampilkan error?**  
A: Kemungkinan besar terjadi kesalahan indentasi (spasi tidak konsisten antara *Tab* dan *Space*) pada kode `.plg` Anda. Pastikan lekukan sejajar layaknya aturan standar Python.

---

## 9. Roadmap Pengembangan

Untuk pengembangan di masa mendatang, proyek ini merencanakan implementasi fitur:

* [ ] Penambahan dukungan tipe data struktur (List, Dictionary, Tuple).
* [ ] Penambahan pustaka standar lokal (contoh: modul untuk memanggil waktu lokal).
* [ ] Integrasi pelapor pesan galat (*Error Handling*) berbahasa Palembang, menggantikan pesan traceback standar dari Python.

---

## 10. Lisensi

Proyek ini menggunakan lisensi perangkat lunak terbuka penuh.

**MIT License**
Copyright (c) 2026.

Izin diberikan dengan cuma-cuma, kepada siapa pun yang mendapatkan salinan perangkat lunak ini dan file dokumentasi terkait ("Perangkat Lunak"), untuk berurusan dengan Perangkat Lunak tanpa batasan, termasuk tanpa batasan hak untuk menggunakan, menyalin, memodifikasi, menggabungkan, menerbitkan, mendistribusikan, mensublisensikan, dan/atau menjual salinan Perangkat Lunak, dengan tunduk pada syarat bahwa pemberitahuan hak cipta di atas harus selalu disertakan dalam semua salinan substansial Perangkat Lunak.
