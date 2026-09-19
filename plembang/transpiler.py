import io
import re
import tokenize

from .keyword import KEYWORDS


class PalembangTranspiler:
    """
    Kelas utama PalembangTranspiler yang bertanggung jawab untuk
    menerjemahkan bahasa pemrograman Baso Palembang menjadi kode
    Python yang valid dan siap dieksekusi oleh mesin.

    Pendekatan yang digunakan adalah kombinasi antara Regular Expressions (RegEx)
    untuk method khusus (Array & File I/O) dan Python Tokenization (tokenize)
    untuk keyword logika utama agar aman serta presisi.
    """

    def __init__(self, keywords: dict[str, str] | None = None) -> None:
        """
        Inisialisasi transpiler dengan memuat kamus kata kunci (keywords)
        dari modul eksternal atau menggunakan kamus bawaan default.
        """
        self.keywords: dict[str, str] = (
            keywords.copy() if keywords is not None else KEYWORDS.copy()
        )

    def _terapkan_regex_khusus(self, kode_sumber: str) -> str:
        """
        Tahap awal: Menerapkan aturan Regular Expressions untuk mengubah
        method bawaan khas Baso Palembang (seperti manipulasi list dan berkas)
        menjadi fungsi setara di dalam standar Python.
        """
        aturan_regex = {
            r"\.tambahke\(": ".append(",
            r"\.buang\(": ".remove(",
            r"\.cabut\(": ".pop(",
            r"\bbuko\(": "open(",
            r"\.baco\(": ".read(",
            r"\.toles_file\(": ".write(",
            r"\.tutup\(": ".close(",
        }

        hasil_transformasi = kode_sumber
        for pola_regex, pengganti_python in aturan_regex.items():
            hasil_transformasi = re.sub(
                pola_regex, pengganti_python, hasil_transformasi
            )

        return hasil_transformasi

    def transpile(self, source_code: str) -> str:
        """
        Fungsi inti (core method) untuk memproses seluruh baris kode sumber
        Baso Palembang dan mengonversinya secara utuh ke dalam format Python.
        """
        if not source_code or not source_code.strip():
            return ""

        # Langkah 1: Jalankan pembersihan menggunakan aturan RegEx khusus
        kode_setelah_regex = self._terapkan_regex_khusus(source_code)

        # Langkah 2: Persiapan tokenisasi menggunakan modul bawaan Python 'tokenize'
        bytes_kode = io.BytesIO(kode_setelah_regex.encode("utf-8"))
        token_termodifikasi: list[tokenize.TokenInfo] = []

        try:
            stream_token = tokenize.tokenize(bytes_kode.readline)

            for token in stream_token:
                # Periksa apakah token merupakan identifier/nama yang terdaftar di kamus
                if token.type == tokenize.NAME and token.string in self.keywords:
                    token_baru = token._replace(string=self.keywords[token.string])
                    token_termodifikasi.append(token_baru)
                else:
                    token_termodifikasi.append(token)

            # Langkah 3: Rekonstruksi token kembali menjadi teks kode program yang valid
            kode_mentah_untokenized = tokenize.untokenize(token_termodifikasi)

            if isinstance(kode_mentah_untokenized, bytes):
                return kode_mentah_untokenized.decode("utf-8")

            return kode_mentah_untokenized

        except tokenize.TokenError as err_tokenisasi:
            # Penanganan error yang ramah pengguna dengan dialek lokal
            pesan_error = f"Ado yang buak sintaks kau pas kode: {err_tokenisasi}"
            raise SyntaxError(pesan_error) from err_tokenisasi
