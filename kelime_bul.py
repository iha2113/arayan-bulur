import subprocess

# Başlık yazdırma
def figlet():
    subprocess.call(["figlet", "Arayan Bulur"])

figlet()

# Kullanıcıdan arama bilgilerini al
kelime = input("🔎 Lütfen aramak istediğiniz kelimeyi giriniz: ")
yol = input("📂 Lütfen dosya yolunu giriniz: ")

try:
    with open(yol, "r", encoding="utf-8", errors="ignore") as f:
        bulundu = False
        for line in f:
            if kelime in line:  # satır içinde kelimeyi ara
                bulundu = True
                break

    if bulundu:
        print(f"✅ Kelime bulundu: {kelime}")
    else:
        print(f"❌ Kelime bulunamadı: {kelime}")

except FileNotFoundError:
    print("⚠️ Dosya yolu hatalı! Lütfen geçerli bir yol giriniz.")
