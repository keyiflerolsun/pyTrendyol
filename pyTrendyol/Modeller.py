# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pydantic import BaseModel

class KategoriUrun(BaseModel):
    link       : str
    marka      : str
    yildiz     : int
    baslik     : str
    indirim    : str | None
    indirimsiz : str | None
    fiyat      : str

class Yorum(BaseModel):
    kullanici : str
    elit      : bool
    tarih     : str
    satici    : str
    yildiz    : int
    yorum     : str

class UrunDetay(BaseModel):
    link      : str
    marka     : str
    baslik    : str
    resim     : str
    gercek    : str | None
    indirimli : str | None
    kampanya  : str | None
    son_fiyat : str
    yorumlar  : list[Yorum]