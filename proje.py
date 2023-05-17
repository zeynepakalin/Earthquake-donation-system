kullanicilar = {}
adminler = {}

# Kullanıcıya seçenekleri göster
print("1.Sisteme üye ol")
print("2.Sisteme giriş yap")
print("3.Şifremi unuttum") 
if secim == "1":
        uye_kayit()
elif secim == "2":
        kullanici_girisi()
elif secim == "3":
        sifre_sifirla()
elif secim == "0":
        print("Çıkış yapılıyor...")
        return
else: 
        print("Geçersiz seçim!")

#Kayıt olma işlemi 
    
email =input("Email adresinizi girin: ")
kullanıcıadı =input("Kullanıcı adınızı girin: ")
kullanicilar[kullanıcıadı] = (ad, soyad, sifre)
while True:
    şifre =input("Şifrenizi belirleyiniz:")
    if len(şifre)<8:
        print("Şifre 8 karakterden az olmamalıdır")
    else:
     print("Şifreniz başarıyla belirlenmiştir.")
     break
 
    
#Sisteme giriş yapma işlemi (2.ye basıldığında)
kullanıcıadı = input("Kullanıcı adınızı girin: ")
 if kullanıcıadı in kullanicilar:
        if kullanicilar[kullanıcıadı][2] == şifre:
            print("Giriş başarılı. Hoş geldiniz, ", kullanıcıadı)
            else:
            print("Hatalı şifre girdiniz!")
    else:
        print("Kullanıcı adınız geçersizdir!")
        
#Şifremi unuttum işlemi (3.ye basıldığında)

şifre = input("Şifremi unuttum")
  if (şifre == Şifremi unuttum):
    print("Yeni şifre belirleyiniz:")
    şifre =input("Şifrenizi belirleyiniz:")
     if len(şifre)<8:
         print("Şifre 8 karakterden az olmamalıdır")
     else:
      print("Şifreniz başarıyla belirlenmiştir.")
  else:
      print("Yeni şifre belirlemenize gerek yoktur")
      break
  
# Admin girişi
def admin_girisi():
    admin_adi = input("Admin kullanıcı adını girin: ")
    sifre = input("Şifrenizi girin: ")
    if admin_adi in adminler:
        if adminler[admin_adi] == sifre:
            print("Admin girişi başarılı. Hoş geldiniz, ", admin_adi, "!")
        else:
            print("Hatalı şifre!")
    else:
        print("Geçersiz admin kullanıcı adı girdiniz.")

# Admin yetkilerini ayarla
def admin_yetkilendirme():
    admin_adi = input("Admin kullanıcı adını belirleyin: ")
    sifre = input("Şifrenizi belirleyin: ")
    adminler[admin_adi] = sifre
    print("Admin yetkilendirmesi tamamlandı!")


# Admin yetkilendirme işlemi
admin_yetkilendirme()

# Ana menüyü başlat
ana_menu()
    

 
 
    
    

