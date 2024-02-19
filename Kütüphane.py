from bs4 import BeautifulSoup
import requests
def veri_çekme():
    sayac=0
     
    
    r = requests.get("https://www.bkmkitap.com/en-cok-okunan-kitaplar")
    source = BeautifulSoup(r.content,"html.parser")
        
    metinler= source.find_all("div",attrs={"class":"col col-12 drop-down hover box-border"})
    url="https://www.bkmkitap.com"
        
    liste=[]
    for metin in metinler:
            baslik= metin.find("a").get("href")
            liste.append(baslik)
        
        
    yeni_linkler=[]
    for i in liste:
            yeni_url=url+i
            yeni_linkler.append(yeni_url)
     
    
    for i in yeni_linkler:
            r1 = requests.get(i)
            source = BeautifulSoup(r1.content,"html.parser")
            metinler1= source.find("h1",attrs={"class":"fl col-12 text-regular m-top m-bottom"}).text
            metinler2= source.find("a",attrs={"id":"productModelText"}).get("title")
            metinler3= source.find_all("div",attrs={"col cilt col-12"})
            
            
            for i in metinler3:
                kaynak = i.find_all("div",attrs={"class":"fl col-6"})[1].text
            
            a =kaynak.split()
            
            metin33=""
            for kelime in a:
                metin33=metin33+kelime
            
            satır="Kitap Adı: {}, {}, {}\n".format(metinler1,metinler2,metin33)
            
            
            print(satır)
            
            
            sayac=sayac+1
            if sayac==10:
                
                break
class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, isim, yazar, basim_tarihi, sayfa_sayisi):
        self.kitaplar.append({
            'isim': isim,
            'yazar': yazar,
            'basim_tarihi': basim_tarihi,
            'sayfa_sayisi': sayfa_sayisi
        })
        self.kitapları_kaydet()

    def kitaplari_listele(self):
        for kitap in self.kitaplar:
            print(f"Kitap İsmi: {kitap['isim']} - Yazar: {kitap['yazar']}")

    def kitap_cikar(self, isim):
        self.kitaplar = [kitap for kitap in self.kitaplar if kitap['isim'] != isim]
        self.kitapları_kaydet()

    def kitapları_kaydet(self):
        with open('kutuphane.txt', 'a+') as dosya:
            for kitap in self.kitaplar:
                dosya.write(f"{kitap['isim']},{kitap['yazar']},{kitap['basim_tarihi']},{kitap['sayfa_sayisi']}\n")
            
    def kutuphane_yukle(self):
        
            with open('kutuphane.txt', 'a+') as dosya:
                for line in dosya:
                    isim, yazar, basim_tarihi, sayfa_sayisi = line.strip().split(',')
                    self.kitaplar.append({
                        'isim': isim,
                        'yazar': yazar,
                        'basim_tarihi': basim_tarihi,
                        'sayfa_sayisi': sayfa_sayisi
                    })
        

kutuphane = Kutuphane()
kutuphane.kutuphane_yukle()

while True:
    print("\nKütüphane Otomasyonu")
    print("1. Kitap Ekle")
    print("2. Kitapları Listele")
    print("3. Kitap Çıkar")
    print("4. En Çok Okunan 10 Kitap")
    print("5. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == '1':
        isim = input("Kitap İsmi: ")
        yazar = input("Yazar: ")
        basim_tarihi = input("Basım Tarihi: ")
        sayfa_sayisi = input("Sayfa Sayısı: ")
        kutuphane.kitap_ekle(isim, yazar, basim_tarihi, sayfa_sayisi)
        print("Kitap eklendi.")

    elif secim == '2':
        kutuphane.kitaplari_listele()

    elif secim == '3':
        isim = input("Çıkarmak istediğiniz kitabın ismini girin: ")
        kutuphane.kitap_cikar(isim)
        print("Kitap çıkarıldı.")

    elif secim == '4':
        veri_çekme()
    elif secim == '5':
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz işlem. Tekrar deneyin.")

