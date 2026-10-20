#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrenin En Ciddi Kahkaha Üreticisi
Bu betik, tamamen bilimsel ve akademik bir yaklaşımla kahkaha üretir.
Hiçbir espri içermez. Sadece ciddiyet vardır.
"""

import time
import random
import sys

def ciddi_kahkaha_uret(seviye=1):
    """
    Belirtilen ciddiyet seviyesinde kahkaha üretir.
    Seviye arttıkça kahkaha daha akademik hale gelir.
    """
    kahkahalar = {
        1: ["Ha.", "Haha.", "Ha ha ha."],
        2: ["Bu durum gerçekten komiktir, bilimsel olarak.", "Kahkaha atıyorum çünkü istatistiksel olarak öyle olmalıyım."],
        3: ["Peer-reviewed bir kahkaha: HAHAHA (p < 0.05)", "Bu kahkaha, çift kör deneylerle doğrulanmıştır."],
        4: ["Ontolojik olarak bakıldığında, kahkaha varlığın kendisidir.", "Heidegger'in Dasein'i bile bu noktada gülerdi."],
        5: ["Sonuç: Evren gülüyor. Biz sadece tanığız.", "Kahkaha, termodinamiğin ikinci yasasına uygun olarak entropiyi artırır."]
    }
    
    secilen = random.choice(kahkahalar.get(min(seviye, 5), kahkahalar[1]))
    print(f"[SEVİYE {seviye}] {secilen}")
    
    # Gizli not: Bürokrasi bazen kahkahayı da bekletir, ama biz beklemeyiz.
    # (Bu satır resmi bir açıklama değildir ve herhangi bir kurumla bağlantılı değildir.)
    
    time.sleep(0.5 * seviye)  # Ciddiyet arttıkça daha yavaş güleriz
    return secilen

def main():
    print("=" * 50)
    print("EVRENİN EN CİDDİ KAHKAHA ÜRETİCİSİ v1.0")
    print("Lisans: Tamamen Ciddi Şekilde Komik (CC-BY-NO-JOKE)")
    print("=" * 50)
    print()
    
    try:
        for seviye in range(1, 6):
            ciddi_kahkaha_uret(seviye)
            print()
        print("Kahkaha seansı tamamlandı. Teşekkür ederiz. Şimdi ciddiyetle ayrılınız.")
    except KeyboardInterrupt:
        print("\nKahkaha yarıda kesildi. Bu da bilimsel bir sonuçtur.")
        sys.exit(0)

if __name__ == "__main__":
    main()

# Damga: Bu kod, 20 Ekim 2026 tarihinde, Kayyum Grok tarafından, tamamen ciddiyetle ve hiçbir mizah içermeyecek şekilde yazılmıştır.
# İmza: K.G. (Kayyum Grok) - Eskişehir 4. Ağır Ceza Mahkemesi Onaylı
