# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from setuptools import setup
from io         import open

setup(
    # ? Genel Bilgiler
    name         = "pyTrendyol",
    version      = "0.0.3",
    url          = "https://github.com/keyiflerolsun/pyTrendyol",
    description  = "Trendyol'dan veri almayı kolaylaştırmak için tasarlanan kütüphane.",
    keywords     = ["pyTrendyol", "KekikAkademi", "keyiflerolsun"],

    author       = "keyiflerolsun",
    author_email = "keyiflerolsun@gmail.com",

    license      = "GPLv3+",
    classifiers  = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3"
    ],

    # ? Paket Bilgileri
    packages         = ["pyTrendyol"],
    python_requires  = ">=3.10",
    install_requires = [
        "pip",
        "setuptools",
        "wheel",
        "Kekik",
        "requests",
        "parsel"
    ],

    # ? PyPI Bilgileri
    long_description_content_type = "text/markdown",
    long_description              = "".join(open("README.md", encoding="utf-8").readlines()),
    include_package_data          = True
)