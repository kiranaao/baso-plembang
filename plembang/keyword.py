"""
keyword.py
Modul khusus pemetaan kato kunci (keywords) dan fungsi bawaan
dari Baso Palembang ke Bahasa Python.
"""

# KAMUS KATO KUNCI (PALEMBANG -> PYTHON)
KEYWORDS: dict[str, str] = {
    # Percabangan (Control Flow)
    "kalu": "if",
    "kalu_bae": "elif",
    "daknyo": "else",

    # Perulangan (Looping)
    "selamo": "while",
    "tiap": "for",
    "didalem": "in",
    "berenti": "break",
    "lanjot": "continue",
    "liwat": "pass",

    # Fungsi & Subroutine 
    "fungsi": "def",
    "balekke": "return",

    # Penanganan Eror (Error Handling)
    "cubo": "try",
    "kecuali": "except",
    "akhernyo": "finally",

    # Logika & Konstanta
    "dan": "and",
    "ato": "or",
    "dakdo": "not",
    "iyo": "True",
    "dak": "False",
    "kosong": "None",

    # Fungsi Bawaan (Built-in Functions)
    "toleske": "print",
    "masukke": "input",
    "banyak": "len",
    "urutan": "range",
    "angko": "int",
    "teks": "str",
    "pecahan": "float",
    "daftar": "list",
    "kamus": "dict",
}

# HELPER FUNCTIONS
def get_python_keyword(word: str) -> str | None:
    """Balekke pasangan kato kunci Python kalu kato Palembang la tedaftar."""
    return KEYWORDS.get(word)


def is_palembang_keyword(word: str) -> bool:
    """Nak ngecek apo suatu identifer tuh kato kunci terdaftar apo bukan."""
    return word in KEYWORDS