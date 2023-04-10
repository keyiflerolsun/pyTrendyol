# Bu araç @kadirilgin1453 tarafından | @KekikAkademi için yazılmıştır.

from Kekik    import slugify
from requests import get
from parsel   import Selector
from typing   import Tuple,List
class Link:
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
        return f"{__class__.__name__} Sınıfı -- Trendyol'dan hedef linkdeki ürünlerini çevirmek için kodlanmıştır."

    def __init__(self):
        """Trendyol'dan hedef linkteki ürünlerini çevirir"""
        self.__kimlik = {"User-Agent": "pyTrendyol"}
        self.parametreler = {
            'culture': 'tr-TR',
            'userGenderId': '1',
            'pId': '0',
            'scoringAlgorithmId': '2',
            'categoryRelevancyEnabled': 'false',
            'isLegalRequirementConfirmed': 'false',
            'searchStrategyType': 'DEFAULT',
            'productStampType': 'TypeA',
            'fixSlotProductAdsIncluded': 'true',
            'searchAbDecider': ',Suggestion_A,Relevancy_1,FilterRelevancy_1,ListingScoringAlgorithmId_1,Smartlisting_2,FlashSales_1,SuggestionBadges_A',
        }

    def urunleri_ver(self, sayfa_linki:str, sayfa_tara:int=1) -> list[dict] or None:
        """ilgili linkteki ürünleri istenilen sayfa sayısı boyunca listeler (her sayfada 24 ürün vardır.)"""

        veriler = []
        for parametre in sayfa_linki.split("?")[1].split("&"):
            self.parametreler[parametre.split("=")[0]] = parametre.split("=")[1]

        for say in range(1, sayfa_tara+1):
            self.parametreler["pi"] = say
            istek   = get("https://public.trendyol.com/discovery-web-searchgw-service/v2/api/infinite-scroll/sr", headers=self.__kimlik,params=self.parametreler)
            urunler = istek.json()["result"]["products"]

            for urun in urunler:
                urun_bilgi = self.urun_ver(urun["id"])
                urun_bilgileri = {
                    "link"       : urun_bilgi["link"],
                    "baslik"     : urun_bilgi["baslik"],
                    "fiyat"      : urun_bilgi["fiyat"],
                    "aciklama"   : urun_bilgi["aciklama"],
                    "varyantlar" : urun_bilgi["varyantlar"],
                    "resimler"   : urun_bilgi["resimler"],
                }
                veriler.append(urun_bilgileri)
            if sayfa_tara <= 1:
                break

        return veriler

    def urun_ver(self,urun_id:str) -> dict:
        params = {
            'sav': 'false',
            'storefrontId': '1',
            'culture': 'tr-TR',
            'linearVariants': 'true',
            'isLegalRequirementConfirmed': 'false',
        }
        veri = get(f'https://public.trendyol.com/discovery-web-productgw-service/api/productDetail/{urun_id}', headers=self.__kimlik, params=params)
        veri = veri.json()

        varyant_bilgileri = [f"Varyant : {i['value']} Fiyat : {i['price']} Stok : {i['inStock']}" for i in self._varyantlar(urun_id=urun_id)]
        varyant_bilgileri = "\n".join(varyant_bilgileri)
        return {
            "link": f"https://www.trendyol.com{veri['result']['url']}",
            "baslik":   veri["result"]["name"],
            "aciklama": "\n".join([aciklama["description"] for aciklama in veri["result"]["contentDescriptions"]]),
            "resimler": [f'https://cdn.dsmcdn.com{resim}' for resim in veri["result"]["images"]],
            "stok": veri["result"]["variants"][0]["stock"],
            "varyant_adi": veri["result"]["variants"][0]["attributeValue"],
            "fiyat": veri["result"]["price"]["sellingPrice"]["value"],
            "varyantlar": varyant_bilgileri,
        }
    
    def _varyantlar(self,urun_id:str) -> dict:
        params = {
            'sav': 'false',
            'storefrontId': '1',
            'culture': 'tr-TR',
            'linearVariants': 'true',
            'isLegalRequirementConfirmed': 'false',
        }
        veri = get(f'https://public.trendyol.com/discovery-web-productgw-service/api/productDetail/{urun_id}', headers=self.__kimlik, params=params)
        return veri.json()["result"]["allVariants"]