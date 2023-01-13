# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from requests            import get
from requests.exceptions import ConnectionError
from urllib.parse        import unquote
from re                  import search, search
from parsel              import Selector

class Urun:
    """
    Urun : Trendyol'dan hedef ürün detaylarını çevirir.

    Methodlar
    ----------
        .detay_ver(link:str) -> dict or None:
            Trendyol'dan hedef ürün detaylarını çevirir
        .yorumlar(self, link:str) -> list[dict] or None:
            Trendyol'dan hedef ürün yorumlarını çevirir
        ._link_ayristir(self, link:str) -> str or None:
            Trendyol'un çeşitli formatlardaki ürün linklerini temizler
    """
    def __repr__(self) -> str:
        return f"{__class__.__name__} Sınıfı -- Trendyol'dan hedef ürün detaylarını çevirmek için kodlanmıştır."

    def __init__(self):
        """Trendyol'dan hedef ürün detaylarını çevirir"""
        self.__kimlik   = {"User-Agent": "pyTrendyol"}
        self.__ayristir = lambda berisi, gerisi, yazi : search(f'{berisi}(.*){gerisi}', yazi).group(1)

    def detay_ver(self, link:str) -> dict or None:
        """Trendyol'dan hedef ürün detaylarını çevirir"""
        link = self._link_ayristir(link)
        if not link:
            return None

        try:
            istek = get(link, headers=self.__kimlik, allow_redirects=True)
        except ConnectionError:
            return None

        secici = Selector(istek.text)

        try:
            return {
                "link"       : link,
                "marka"      : secici.xpath("//h1[@class='pr-new-br']/a/text()").get().strip() if secici.xpath("//h1[@class='pr-new-br']/a/text()").get() else secici.xpath("//h1[@class='pr-new-br']/text()").get().strip(),
                "baslik"     : secici.xpath("//h1[@class='pr-new-br']/span/text()").get().strip(),
                "resim"      : secici.xpath("//div[@class='gallery-modal-content']//img/@src").get(),
                "gercek"     : secici.xpath("//span[@class='prc-org']/text()").get(),
                "indirimli"  : secici.xpath("//span[@class='prc-slg prc-slg-w-dsc']/text()").get() or secici.xpath("//span[@class='prc-slg']/text()").get(),
                "kampanya"   : secici.xpath("//div[@class='pr-bx-pr-dsc']/text()").get(),
                "son_fiyat"  : secici.xpath("//span[@class='prc-dsc']/text()").get(),
                "yorumlar"   : self.yorumlar(link),
            }
        except AttributeError:
            return None

    def yorumlar(self, link:str) -> list[dict] or None:
        """Trendyol'dan hedef ürün yorumlarını çevirir"""
        link = self._link_ayristir(link)
        if not link:
            return None

        yorumlar = []

        url     = f"https://public-mdc.trendyol.com/discovery-web-socialgw-service/api/review/{link.split('-')[-1]}"
        istek   = get(url, headers=self.__kimlik)
        veriler = istek.json()["result"]["productReviews"]

        sayfa = 1
        while True:
            yorumlar.extend(
                {
                    "kullanici" : yorum["userFullName"],
                    "elit"      : yorum["isElite"],
                    "tarih"     : yorum["lastModifiedDate"],
                    "satici"    : yorum["sellerName"],
                    "yildiz"    : yorum["rate"],
                    "yorum"     : yorum["comment"]
                }
                    for yorum in veriler["content"]
            )

            sayfa += 1
            if sayfa == veriler["totalPages"]:
                break

            istek   = get(f"{url}?page={sayfa}", headers=self.__kimlik)
            veriler = istek.json()["result"]["productReviews"]

        return yorumlar

    def _link_ayristir(self, link:str) -> str or None:
        """Trendyol'un çeşitli formatlardaki ürün linklerini temizler"""
        if link.startswith('https://m.'):
            url = link.replace('https://m.', 'https://')
        elif link.startswith('https://ty.gl'):
            try:
                kisa_link_header = get(link, headers=self.__kimlik, allow_redirects=False).headers['location']
                url = self.__ayristir("adjust_redirect=", "&adjust_t=", unquote(kisa_link_header))
            except KeyError:
                url = None
        else:
            url = link if search(r"http(?:s?):\/\/(?:www\.)?(m?.)?t?", link) else None

        return url.split('?')[0].replace('www.', '') if url else None