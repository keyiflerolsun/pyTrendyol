# ![pyTrendyol](https://cdn.dsmcdn.com/web/production/favicon.ico) pyTrendyol

![Repo Boyutu](https://img.shields.io/github/repo-size/keyiflerolsun/pyTrendyol?logo=git&logoColor=white)
![Görüntülenme](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/keyiflerolsun/pyTrendyol&title=Görüntülenme)
<a href="https://KekikAkademi.org/Kahve" target="_blank"><img src="https://img.shields.io/badge/☕️-Kahve Ismarla-ffdd00" title="☕️ Kahve Ismarla" style="padding-left:5px;"></a>

![Python Version](https://img.shields.io/pypi/pyversions/pyTrendyol?logo=python&logoColor=white)
![License](https://img.shields.io/pypi/l/pyTrendyol?logo=gnu&logoColor=white)
![Status](https://img.shields.io/pypi/status/pyTrendyol?logo=windowsterminal&logoColor=white)

![PyPI](https://img.shields.io/pypi/v/pyTrendyol?logo=pypi&logoColor=white)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyTrendyol?logo=pypi&logoColor=white)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/pyTrendyol?logo=pypi&logoColor=white)

[![PyPI Yükle](https://github.com/keyiflerolsun/pyTrendyol/actions/workflows/pypiYukle.yml/badge.svg)](https://github.com/keyiflerolsun/pyTrendyol/actions/workflows/pypiYukle.yml)

*Trendyol'dan veri almayı kolaylaştırmak için tasarlanan kütüphane.*

[![ForTheBadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](https://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

## 🚀 Kurulum

```bash
# Yüklemek
pip install pyTrendyol

# Güncellemek
pip install -U pyTrendyol
```

## 📝 Kullanım

```python
from pyTrendyol import Kategori, Urun

trend_kategori = Kategori()
trend_urun     = Urun()

telefon_aksesuarlari = trend_kategori.urunleri_ver(
    kategori_adi = "telefon aksesuarları",
    sayfa_tara   = 3
)
print(telefon_aksesuarlari[0])
# KategoriUrun(
#     link='https://www.trendyol.com/kvk-privacy/iphone-13-ve-14-uyumlu-hologramli-love-desenli-seffaf-kilif-p-362588758',
#     marka='KVK PRİVACY',
#     yildiz=4,
#     baslik='Iphone 13 Ve 14 Uyumlu Hologramlı Love Desenli Şeffaf Kılıf',
#     indirim=None,
#     indirimsiz=None,
#     fiyat='103,05 TL'
# )

urun_detay = trend_urun.detay_ver(
    urun_link = "https://trendyol.com/creative/stage-2-1-160w-kablosuz-bluetooth-soundbar-p-98119546"
)
print(urun_detay)
# UrunDetay(
#     link='https://trendyol.com/creative/stage-2-1-160w-kablosuz-bluetooth-soundbar-p-98119546',
#     marka='Creative',
#     baslik='Stage 2.1 160w Kablosuz Bluetooth Soundbar',
#     resim='https://cdn.dsmcdn.com/mnresize/1200/1800/ty102/product/media/images/20210413/13/79756771/163316178/1/1_org_zoom.jpg',
#     gercek='4.399 TL',
#     indirimli=None,
#     kampanya=None,
#     son_fiyat='4.097 TL',
#     yorumlar=[
#         Yorum(
#             kullanici='Hakan T.',
#             elit=False,
#             tarih='9 Temmuz 2021',
#             satici='ConnectGame',
#             yildiz=5,
#             yorum='Gayet güzel sesi bas vurması ama bi noktadan sonra buda yetmiyebilir 😂'
#         )
#     ]
# )
```

## 💸 Bağış Yap

**[☕️ Kahve Ismarla](https://KekikAkademi.org/Kahve)**

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2023 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/pyTrendyol/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/KekikKahve)

##

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*