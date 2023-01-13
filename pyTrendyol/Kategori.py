# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kekik    import slugify
from requests import get
from parsel   import Selector

class Kategori:
    """
    Kategori : Trendyol'dan hedef kategori ürünlerini çevirir.

    Methodlar
    ----------
        .urunleri_ver(kategori_adi:str, sayfa_tara:int=1) -> list[dict] or None:
            ilgili kategori ürünlerini istenilen sayfa sayısı boyunca listeler (her sayfada 24 ürün vardır.)
        .mevcut_mu(kategori_adi:str) -> bool:
            ilgili kategori mevcut mu değil mi bilgisini verir
        .kategoriler -> dict[str, str]:
            mevcut kategorileri trendyol rss'inden ayrıştırıp çevirir
    """
    def __repr__(self) -> str:
        return f"{__class__.__name__} Sınıfı -- Trendyol'dan hedef kategori ürünlerini çevirmek için kodlanmıştır."

    def __init__(self):
        """Trendyol'dan hedef kategori ürünlerini çevirir"""
        self.__kimlik = {'User-Agent': 'pyTrendyol'}
        self.kategoriler = self.__kategoriler

    def urunleri_ver(self, kategori_adi:str, sayfa_tara:int=1) -> list[dict] or None:
        """ilgili kategori ürünlerini istenilen sayfa sayısı boyunca listeler (her sayfada 24 ürün vardır.)"""
        kategori_adi = self.__ascii_decode(kategori_adi)
        if not self.mevcut_mu(kategori_adi):
            return None

        veriler = []
        for say in range(1, sayfa_tara+1):
            istek   = get(f"https://www.trendyol.com/{kategori_adi}{self.kategoriler[kategori_adi]}?pi={say}", headers=self.__kimlik)
            secici  = Selector(istek.text)

            urunler = secici.xpath("//div[@class='prdct-cntnr-wrppr']//div[contains(@class, 'p-card-chldrn')]")

            for urun in urunler:
                yildiz_sayisi = 0
                for i_yildiz in urun.xpath(".//div[@class='ratings']/div"):
                    yildiz = list(i_yildiz.xpath(".//div[@class='full' and @style='width:100%;max-width:100%']"))

                    yildiz_sayisi += len(yildiz)

                urun_bilgileri = {
                    "link"       : "https://www.trendyol.com" + urun.xpath(".//a/@href").get(),
                    "marka"      : urun.xpath(".//span[@class='prdct-desc-cntnr-ttl']/text()").get(),
                    "yildiz"     : yildiz_sayisi,
                    "baslik"     : urun.xpath(".//span[@class='prdct-desc-cntnr-name hasRatings']/text()").get() or urun.xpath(".//span[@class='prdct-desc-cntnr-name']/text()").get(),
                    "indirim"    : urun.xpath("normalize-space(.//div[@class='pr-bx-pr-dsc-pr'])").get() or None,
                    "indirimsiz" : urun.xpath("normalize-space(.//div[@class='prc-box-sllng prc-box-sllng-w-dscntd'])").get() or None,
                    "fiyat"      : urun.xpath("normalize-space(.//div[@class='product-price'])").get() or urun.xpath("normalize-space(.//div[@class='prc-box-dscntd'])").get()
                }
                veriler.append(urun_bilgileri)
            if sayfa_tara <= 1:
                break

        return veriler

    def mevcut_mu(self, kategori_adi:str) -> bool:
        """mevcut kategorileri trendyol rss'inden ayrıştırıp çevirir"""
        return self.__ascii_decode(kategori_adi) in self.kategoriler

    @property
    def __kategoriler(self) -> dict[str, str]:
        """mevcut kategorileri trendyol rss'inden ayrıştırıp çevirir"""
        sitemap = get('https://www.trendyol.com/sitemap_categories.xml', headers=self.__kimlik)
        secici  = Selector(sitemap.text)

        linkler = [link.replace('https://m.trendyol.com/', '') for link in secici.xpath('//@href').getall()]

        return {link.split('-x-')[0].replace("https://www.trendyol.com/", "") : f"-x-{link.split('-x-')[1]}" for link in linkler}

    @staticmethod
    def __ascii_decode(metin:str) -> str:
        tr2eng  = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")
        return slugify(metin.translate(tr2eng)).replace('_','-')