# Kullanıcıya seçenekleri göster
#Choice kısmını daha görmediğimiz için eklemedim
print("1.Sisteme üye ol")
print("2.Sisteme giriş yap")
print("3.Şifremi unuttum") 

#Kayıt olma işlemi 
    
email =input("Email adresinizi girin: ")
kullanıcıadı =input("Kullanıcı adınızı girin: ")
while True:
    şifre =input("Şifrenizi belirleyiniz:")
    if len(şifre)<8:
        print("Şifre 8 karakterden az olmamalıdır")
    else:
     print("Şifreniz başarıyla belirlenmiştir.")
     break
 
    
#Sisteme giriş yapma işlemi (2.ye basıldığında)
kullanıcıadı = input("Kullanıcı adınızı girin: ")
şifre = input("Şifrenizi girin: ")
while True:
    şifre = input("Şifrenizi girin:")
    if şifre:
        print("Başarıyla giriş yaptınız.")
        
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
    

 
 
    
    

