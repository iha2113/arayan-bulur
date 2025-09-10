# Arayan Bulur 🔎

**Arayan Bulur**, terminal üzerinde çalışan basit ve kullanıcı dostu bir **dosya içinde kelime arama aracıdır**.  
Figlet ile şık bir başlık gösterir ve aranan kelimenin dosya içinde bulunup bulunmadığını belirtir.

---

## Özellikler
- Terminal üzerinde çalışır
- Dosya içinde kelime arama
- Büyük/küçük harf duyarsız arama (opsiyonel)
- Dosya bulunamazsa uyarı verir
- Kullanıcı dostu simgeler ile sonuç gösterimi (✅❌⚠️)

---

## Kullanım

1. Depoyu klonlayın:
```bash
git clone https://github.com/kullaniciadi/arayan-bulur.git

2. Python dosyasını çalıştırın:

python arayan_bulur.py


3. İstenilen bilgileri girin:
-Aranacak kelime
-Dosya yolu

4. Sonuç terminalde gösterilecektir.

Örnek
🔎 Lütfen aramak istediğiniz kelimeyi giriniz: python
📂 Lütfen dosya yolunu giriniz: deneme.txt
✅ Kelime bulundu: python

Gereksinimler

Python 3.x

figlet (Linux / Mac için)

sudo apt install figlet   # Debian / Ubuntu
brew install figlet       # Mac
