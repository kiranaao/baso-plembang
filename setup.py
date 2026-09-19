import os
import re

from setuptools import find_packages, setup  # type: ignore


def get_version() -> str:
    """Ngebacoi versi secaro dinamis dari __init__.py."""
    init_path = os.path.join("plembang", "__init__.py")
    try:
        with open(init_path, "r", encoding="utf-8") as f:
            match = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read())
            if match:
                return match.group(1)
    except FileNotFoundError:
        pass
    return "0.1.0"


def get_long_description() -> str:
    """Ngebacoi README.md untuk dijadike deskripsi panjang otomatis."""
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Transpiler dan Runtime Engine untuk Esolang Baso Plembang"


setup(
    name="baso-plembang",
    version=get_version(),
    author="Kiranaao",
    author_email="kiranaaozoe@gmail.com",
    description="Transpiler dan Runtime Engine untuk Bahasa Pemrograman Baso Plembang",
    long_description=get_long_description(),
    long_description_content_type="Transpiler dan runtime engine bahasa pemrograman lokal Baso Plembang berbasis Python. \nDigunakan untuk keperluan belajar bagi pemula menggunakan bahasa Palembang.",
    url="https://github.com/kiranaao/baso-plembang",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "plembang=plembang.cli:main",
        ],
    },
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Interpreters",
    ],
    keywords="esolang palembang transpiler language compiler",
)