# 🐟 Baso Plembang

**Baso Plembang** adalah _esoteric programming language_ (esolang) berorientasi _transpiler_ berbasis Python. Bahasa pemrograman ini dirancang menggunakan sintaks, struktur logika, dan kosakata lokal dari bahasa Palembang, Sumatra Selatan.

Proyek ini dikembangkan sebagai portofolio teknis dan media edukasi inovatif. Tujuannya adalah untuk menurunkan batas masuk (_barrier to entry_) bagi pemula yang ingin mempelajari algoritma dan logika komputasi dengan cara yang lebih merakyat, kontekstual, dan menyenangkan tanpa harus bingung oleh bahasa Inggris teknis.

---

## 📑 Daftar Isi

1. [Fitur Utama](#-fitur-utama)
2. [Kamus Kosakata Sintaks](#-kamus-kosakata-sintaks)
3. [Panduan Lengkap Pengguna (User)](#-panduan-lengkap-pengguna-user)
   - [1. Instalasi Ekstensi VS Code (.vsix)](#1-instalasi-ekstensi-vs-code-vsix)
   - [2. Cara Menulis dan Menjalankan Kode](#2-cara-menulis-dan-menjalankan-kode)
4. [Panduan Lengkap Developer (Kontributor)](#️-panduan-lengkap-developer-kontributor)
   - [1. Kloning dan Struktur Direktori](#1-kloning-dan-struktur-direktori)
   - [2. Cara Build Ulang Ekstensi](#2-cara-build-ulang-ekstensi)
5. [Contoh Program Komprehensif](#-contoh-program-komprehensif)
6. [Lisensi](#-lisensi)

---

## 💡 Fitur Utama

- **Logika Berbasis Python**: Arsitektur bahasa ini mengadopsi 100% aturan _indentation_ (spasi/tab) dan logika eksekusi Python. Kode yang kamu tulis diubah (_transpile_) menjadi Python secara _real-time_.
- **Pewarnaan Sintaks Otomatis (Syntax Highlighting)**: Dilengkapi dengan ekstensi mandiri Visual Studio Code (`.vsix`) sehingga kode yang ditulis tidak terlihat sebagai teks mati (_plain text_), melainkan berwarna cerah seperti bahasa pemrograman standar industri.
- **Eksekutor Portabel (Standalone Runner)**: Tidak membutuhkan instalasi _environment_ Python yang rumit di komputer target. Cukup gunakan file `plembang.exe` atau skrip `run.bat` untuk mengeksekusi program seketika.

---

## 📖 Kamus Kosakata Sintaks

Untuk menjembatani logika Python standar ke dalam Baso Plembang, proyek ini memetakan beberapa kata kunci (_keywords_) utama:

| Fungsi / Logika Python | Sintaks Baso Plembang | Keterangan Tambahan                                         |
| :--------------------- | :-------------------- | :---------------------------------------------------------- |
| `print()`              | `toleske()`           | Mencetak teks atau variabel ke layar terminal.              |
| `input()`              | `masukke()`           | Meminta masukan data dari pengguna sistem.                  |
| `int()`                | `angko()`             | Mengonversi nilai atau input teks menjadi angka bulat.      |
| `def`                  | `fungsi`              | Mendeklarasikan sebuah fungsi baru.                         |
| `return`               | `balekke`             | Mengembalikan nilai dari sebuah fungsi.                     |
| `if`                   | `kalu`                | Blok percabangan kondisi logika.                            |
| `else:`                | `daknyo:`             | Kondisi alternatif jika percabangan `kalu` tidak terpenuhi. |
| `True`                 | `iyo`                 | Nilai _boolean_ benar.                                      |
| `False`                | `dak`                 | Nilai _boolean_ salah.                                      |

---

## 🚀 Panduan Lengkap Pengguna (User)

Bagian ini ditujukan bagi pengguna yang hanya ingin **memakai**, **menulis kode**, dan **menjalankan program** tanpa memodifikasi kode sumber mesin (_backend_).

### 1. Instalasi Ekstensi VS Code (.vsix)
Langkah ini sangat penting agar kodemu berwarna dan terformat dengan rapi di dalam editor.
1. Masuk ke halaman **Releases** di repositori GitHub ini (menu ada di bilah sebelah kanan).
2. Unduh file instalasi ekstensi bernama **`baso-plembang-syntax-1.0.0.vsix`**.
3. Buka aplikasi **Visual Studio Code (VS Code)** di komputermu.
4. Buka menu **Extensions** yang berada di panel sebelah kiri (atau gunakan _shortcut_ `Ctrl+Shift+X`).
5. Pada bagian atas panel Extensions, klik ikon **titik tiga (...)** yang bertuliskan _Views and More Actions_.
6. Pilih opsi **Install from VSIX...** dari menu tarik-turun (_dropdown_).
7. Temukan dan pilih file `baso-plembang-syntax-1.0.0.vsix` yang baru saja kamu unduh, lalu klik tombol **Install**.
8. Notifikasi sukses akan muncul di pojok kanan bawah. Ekstensi resmi siap digunakan.

### 2. Cara Menulis dan Menjalankan Kode
1. Di dalam VS Code, buat file baru dan simpan dengan akhiran **`.plg`** (contoh: `programku.plg`).
2. Pastikan indikator bahasa di pojok kanan bawah layar VS Code sudah menunjukkan tulisan **Baso Plembang** (bukan _Plain Text_). Jika masih _Plain Text_, klik tulisan tersebut dan ketik pencarian "Baso Plembang".
3. Tulis kode programmu (silakan lihat bab Contoh Program di bawah sebagai referensi).
4. Untuk mengeksekusi kode tersebut, unduh file **`plembang.exe`** dari halaman *Releases*.
5. Buka Terminal komputermu di dalam folder tempat penyimpanan kodemu, lalu jalankan perintah:
   ```bash
   plembang.exe programku.plg
