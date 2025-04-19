"""#Bugünün Tarihi ile Kayıt Oluşturulma Tarihi Arasındaki Gün Farkı:
TODAY() - CreatedDate


#Bir Tarihin Hafta Sonu Olup Olmadığını Kontrol Et:
CASE(MOD(DATEVALUE(CreatedDate) - DATE(1985,6,24),7), 0,"Pazar",6,"Cumartesi","Hafta içi")

#Kayıt 30 Günden Eski mi?
TODAY() - DATEVALUE(CreatedDate) > 30

#İki Tarih Arasında İş Gününü Hesapla (Tahmini):

(FLOOR((End_Date__c - Start_Date__c) / 7) * 5) +
MIN(5, MOD(End_Date__c - Start_Date__c, 7))

#Yalnızca Ay Bilgisini Getir (CreatedDate):
MONTH(CreatedDate)


Sayısal ve Mantıksal Formüller

#%18 KDV Hesapla:
Amount__c * 0.18


#İndirimli Fiyat Hesabı:
Price__c - (Price__c * Discount__c / 100)

#Skor Sınırı Geçti mi?
IF(Score__c >= 70, "Geçti", "Kaldı")

#İki Alan Toplamı 100'den Büyükse Uyarı Mesajı:
IF(Field1__c + Field2__c > 100, "Limit Aşıldı", "Uygun")

#Negatif Sayıysa “Uyarı” Dön:
IF(Number_Field__c < 0, "Uyarı: Negatif!", "")

# Kullanıcı ve Sahiplik Formülleri
#Sadece Belirli Bir Profil Girdiyse İşaretle:
$Profile.Name = "Satış Temsilcisi"

#Sahibi Mevcut Kullanıcı mı?
OwnerId = $User.Id

#Kullanıcının Dil Tercihi İngilizce mi?
$User.Language = "en_US"

#Kullanıcının Bölgesi Türkiye mi?
$User.Country = "Turkey"

#Kayıt Sahibi Belirli Bir Kişiyse Etiketle:
IF(OwnerId = "005XXXXXXXXXXXX", "Ana Kişi", "")


#Metin İşlemleri
#Ad ve Soyadı Birleştir:
FirstName & " " & LastName


#E-posta Alanından Domain’i Çek:
RIGHT(Email, LEN(Email) - FIND("@", Email))


#Açıklama 100 Karaktere Kadar Kısalt:
LEFT(Description, 100)


#Boş Alanlara Varsayılan Değer Ver:
IF(ISBLANK(Custom_Field__c), "Bilinmiyor", Custom_Field__c)


#Özel Mesaj Formatı:
"Merhaba " & FirstName & ", kaydınız oluşturuldu!"


##Picklist ve Checkbox Formülleri
#Picklist Seçimine Göre İndirim Uygula:

IF(ISPICKVAL(Category__c, "Öğrenci"), Price__c * 0.90, Price__c)


#Checkbox Seçiliyse “Evet” Yazdır:
IF(Checkbox__c, "Evet", "Hayır")


#Picklist ile Görev Önceliğini Belirle:
CASE(Priority__c, "Yüksek", "!!!", "Orta", "!!", "Düşük", "!", "")

#Seçim "Red" ise Uyarı Göster:
IF(TEXT(Status__c) = "Red", "Onaylanmadı", "")


#Birden Fazla Picklist Şartı:
AND(
ISPICKVAL(Stage__c, "Closed Won"),
ISPICKVAL(Contract_Signed__c, "Hayır")
)


#İlişkili Alan Boşsa Uyarı:
ISBLANK(Account.Name)


#Fırsat 100K üstü ve "Hot" ise:
AND(
Amount > 100000,
ISPICKVAL(Rating, "Hot")
)
#Ödeme Durumu “Ödendi” ve Tarih Geçtiyse Uyarı Verme:
NOT(AND(
ISPICKVAL(Payment_Status__c, "Ödendi"),
Payment_Date__c < TODAY()
))

#Sadece Hafta İçi Günlerinde Aktif Olan Kayıt:
CASE(MOD(TODAY() - DATE(1985,6,24), 7), 0, FALSE, 6, FALSE, TRUE)


#Fırsat Sahibi ve Oluşturan Kullanıcı Aynıysa “Otomatik”:
IF(CreatedById = OwnerId, "Otomatik", "Manuel")"""