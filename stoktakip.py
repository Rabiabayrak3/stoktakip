
"""RABİA BAYRAK"""

stoklar={}
def urun_ekle():
    print(""" 01- hammade \n 02-yarımamul \n 03-Mamul
          """)
    ürün_tipi=int(input("Ürün tipini giriniz: "))
    kod = int(input("Ürün kodunu giriniz: "))
    ad = input("Ürün adı: ")
    miktar = int(input("Miktar: "))

    if kod in stoklar:
        stoklar[kod]['miktar'] += miktar
        print(f"{kod} kodlu ürün başarıyla güncellendi.\n")
    else:
        stoklar[kod] = {'ürün tipi': ürün_tipi ,'kod': kod,'ad': ad, 'miktar': miktar}

    print(f"{kod} kodlu ürün başarıyla eklendi\n")

def urun_cikar():
    kod = int(input("Çıkarmak istediğiniz ürün kodu: "))
    miktar = int(input("Miktar: "))

    if kod in stoklar and stoklar[kod]['miktar'] >= miktar:
        stoklar[kod]['miktar'] -= miktar
        print(f"{miktar} adet ürün çıkarıldı.\n")
        if stoklar[kod]['miktar'] == 0:
            del stoklar[kod]
    else:
        print("Yetersiz stok veya ürün bulunamadı.\n")

def stok_goruntule():
    if not stoklar:
        print("Stokta ürün yok.\n")
    else:
        print("\n--- Stok Durumu ---")
        for kod, bilgi in stoklar.items():
            # Ürün tipi, sayı yerine anlamlı bir metin olarak gösterilecek
            if bilgi['ürün tipi'] == 1:
                urun_tipi = "Hammadde"
            elif bilgi['ürün tipi'] == 2:
                urun_tipi = "Yarı Mamul"
            elif bilgi['ürün tipi'] == 3:
                urun_tipi = "Mamul"
            else:
                urun_tipi = "Bilinmiyor"  # Eğer yanlış bir tür girildiyse

            print(f"Ürün Tipi: {urun_tipi} | Kod: {kod} | Ürün: {bilgi['ad']} | Miktar: {bilgi['miktar']}")
        print()

def menu():
    while True:
        print("1. Ürün Ekle")
        print("2. Ürün Çıkar")
        print("3. Stok Durumu Görüntüle")
        print("4. Çıkış\n")
        secim = input("Seçiminiz: ")

        if secim == "1":
            urun_ekle()
        elif secim == "2":
            urun_cikar()
        elif secim == "3":
            stok_goruntule()
        elif secim == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!\n")

menu()