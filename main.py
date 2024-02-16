# print('Phyton ile ilk günüm!')
# #başına kare koyunca o satır yorum satırı oluyor  yani not  alma satırı
# print("Fonksiyon şu şekilde tanımlanır: print('ekrana yazdırılacak yazı')")

# print("Merhaba Dünya\nMerhaba Dünya\nMerhaba Dünya\n")

#print("Merhaba Dünya")
#print("Merhaba Dünya")
#print("Merhaba Dünya")

# print("Merhaba"+" "+"ahmet")
# print("Merhaba"+"ahmet")
# print("Merhaba"+"ahmet")

# print(input("Merhaba, Adın Nedir?"))


# print("Merhaba " + input("Merhaba,Adın Nedir?") + "!" 

#print(len(input("Merhaba, Adın Nedir?")))

# print(len(str(1234567890))) 
# print("Merhaba"[0])


# print(123 + 456) 
# print(123_456_789) 


# print(3.12345)


# print(True)
# print(False)

# isimUzunluk = len(input("Merhaba, Adın Ne?"))
isimUzunluk_Str = str(isimUzunluk)
print("İsminde " + isimUzunluk_Str + " karakter var.") 1 karakter var.

fl = float(1.322)
print(type(fl))

intt = int(232)
print(type(intt))

st = str(123123)
print(type(st))

print(100 + float(15.23))
print(str(122) +str(324))

ikihanelisayi = str(input("İki haneli bir sayı giriniz!"))
toplam = int(ikihanelisayi[0]) + int(ikihanelisayi[1])
print("Toplam: " + str(toplam))

print(input("Merhaba, Adın Nedir?"))

print("Merhaba " + input("Merhaba,Adın Nedir?") + "!")

print(len(input("Merhaba, Adın Nedir?")))

name = input("Merhaba Adın Nedir?")
print(name)

name = "Ahmet"
print(name)
name = "Demir"
print(name)

print(len(input("Merhaba, Adın Nedir?")))
isim = input("Merhaba, Adın Nedir?")
uzunluk = len(isim)
print(uzunluk)

print("Lunaparka hoşgeldiniz!")
print("bilet fiyatı yetişkin 10 TL. 12 yaşından küçükler 5TL")
boy = int(input("Lütfen boyunuzu giriniz!(cm)"))
yas = int(input("Lütfen yaşınızı giriniz."))
biletfiyati = 0
if boy > 80 :
    if(yas < 12):
        biletfiyati = 5
    else:
        biletfiyati = 10
        print(f"Çarpışan Arabalara binebilirsiniz! Fiyat {bilet fiyati} TL" )
elif boy > 80 and boy < 120:
    if(yas < 12):
        biletfiyati = 5
    else:
        biletfiyati = 10
    print(f"Lunapark Hız Trenine binebilirsiniz! Fiyat {biletfiyati} TL")
elif boy > 120 and boy < 140:
    if(yas < 12):
        biletfiyati = 5
    else:
        biletfiyati = 10
    print(f"Gondola binebilirsiniz! Fiyat {biletfiyati} TL")
elif boy > 140:
    if(yas < 12):
        biletfiyati = 5
    else:
        biletfiyati=10
        print (f"kamikazeye binebilirsiniz! Fiyat {bilet fiyatı}TL")
else:
    print ("Lunaparkta herhangi bir araca binmek için boyunuz yetmiyor!")

sayi = int(input("Lütfen tek mi çift mi olduğunu öğrenmek için bir sayı giriniz"))
kalan = sayi % 2
if kalan == 0:
    print("Girdiğiniz sayı bir çift sayıdır!")
else:
    print("Girdiğiniz sayı bir tek sayıdır!")

boy  = float(input("Boyunuzu giriniz (m): "))
kilo = float(input("Kilonuzu giriniz (kg):"))

vki = int(kilo/boy**2)
if vki < 18.5:
    print(f"Vücut Kitle İndeksiniz: {vki} , Zayıfsınız!")
elif vki > 18.5 and vki < 25:
    print(f"Vücut Kitle İndeksiniz: {vki} , Kilonuz Normal")
elif vki > 25 and vki < 30:
    print(f"Vücut Kitle İndeksiniz: {vki} , Kilolusunuz")
elif vki > 30 and vki < 35:
    print(f"Vücut Kitle İndeksiniz: {vki} , Obezsiniz")
elif vki > 35:
    print(f"Vücut Kitle İndeksiniz: {vki} , Aşırı Kilolusunuz")

    yil = int(input("Hangi yılı kontrol etmek istiyorsunuz?"))
if yil % 4 == 0:
    if yil % 100 == 0:
        if yil % 400 == 0:
            print(f"{yil} bir artık yıldır!")
        else:
         print(f"{yil} bir artık yıl değildir!.")
    else:
         print(f"{yil} bir artık yıl değildir!.")
else:
    print(f"{yil} bir artık yıl değildir!.")

    print("Lunaparka hoşgeldiniz!")
boy = int(input("Boyunuz kaç cm ?"))
ucret =0
if boy >=  120:
    print("Rollercoastera binebilirsiniz!")
    yas = int(input("Kaç yaşındasınız?"))
    if yas < 12:
        ucret = 5
    elif yas <= 18:
        ucret = 10
    else:
        ucret = 20 
        fotografistiyor = input("Fotoğraf çektirmek istiyor musunuz E veya H")
if fotografistiyor == "E":
    ucret += 3
    print(f"Toplam ödeme: {ücret}")
else:
    print ("Üzgünüm boyunuz rollercostera binmek için yeterli değil!")

boy  = float(input("Boyunuzu giriniz (m): "))
kilo = float(input("Kilonuzu giriniz (kg):"))

vki = int(kilo/boy**2)
if vki < 18.5:
    print(f"Vücut Kitle İndeksiniz: {vki} , Zayıfsınız!")
elif vki > 18.5 and vki < 25:
    print(f"Vücut Kitle İndeksiniz: {vki} , Kilonuz Normal")
elif vki > 25 and vki < 30:
    print(f"Vücut Kitle İndeksiniz: {vki} , Kilolusunuz")
elif vki > 30 and vki < 35:
    print(f"Vücut Kitle İndeksiniz: {vki} , Obezsiniz")
elif vki > 35:
    print(f"Vücut Kitle İndeksiniz: {vki} , Aşırı Kilolusunuz") 

print("Sevgi Hesaplayıcıya hoş geldiniz!")
isim1 = input("Adınız Nedir?")
isim2 = input("Onun Adı Nedir?")

isimler = ( isim1 + isim2 ).lower()

g = isimler.count("g")
e = isimler.count("e")
r = isimler.count("r")
ç = isimler.count("ç")
e = isimler.count("e")
k = isimler.count("k")
a = isimler.count("a")
ş = isimler.count("ş")
k = isimler.count("k")


toplam = g + e + r + ç + e + k + a + ş + k

if( toplam < 10 and toplam > 90):
    print(f"Sevgi Puanınız: {toplam}, kola mentos gibisiniz!") 
elif( toplam > 40 and toplam < 50):
    print(f"Sevgi Puanınız {toplam},beraber iyisiniz")
    
    else:
    print(f"Sevgi Puanınız: {toplam}")