#1. Contact üzerinde boş telefon numarasını engelle

ISBLANK(Phone)
Hata Mesajı: "Telefon numarası zorunludur."

#2. Email adresinde @ işareti yoksa hata ver

NOT(CONTAINS(Email, "@"))
Hata Mesajı: "Geçerli bir e-posta adresi girin."

# 3. Doğum tarihi gelecekte olamaz (Contact)

Birthdate > TODAY()
Hata Mesajı: "Doğum tarihi bugünden sonraki bir tarih olamaz."

✅#4. Fırsat tutarı negatif olamaz (Opportunity)

Amount < 0
Hata Mesajı: "Tutar negatif olamaz."

#5. Account oluşturulurken sektör alanı boş olamaz

ISBLANK(Industry)
Hata Mesajı: "Lütfen sektör bilgisini girin."
# 6. Lead üzerinde telefon ve e-posta ikisi de boşsa hata

AND(ISBLANK(Phone), ISBLANK(Email))
Hata Mesajı: "Telefon veya e-posta bilgisinden en az biri girilmelidir."

# 7. Posta kodu yalnızca 5 haneli sayı olabilir

NOT(REGEX(BillingPostalCode, "\\d{5}"))
Hata Mesajı: "Posta kodu 5 haneli bir sayı olmalıdır."

#8. Contact üzerindeki yaş 18’den küçükse uyarı ver

TODAY() - Birthdate < 6570
Hata Mesajı: "18 yaşından küçük kişiler kayıt edilemez."

# 9. Opportunity kapanırken ‘Sebep’ alanı boş olmamalı

AND(
ISPICKVAL(StageName, "Closed Lost"),
ISBLANK(Loss_Reason__c)
)
Hata Mesajı: "Kayıp sebebi doldurulmalıdır."

#10. Task açıklaması en az 10 karakter olmalı

LEN(Description) < 10
Hata Mesajı: "Açıklama en az 10 karakter olmalıdır."

# 11. Email adresi .com ile bitmeli

NOT(REGEX(Email, ".*\\.com$"))
Hata Mesajı: "E-posta .com ile bitmelidir."

# 12. Custom Object üzerinde fiyat 1000’den büyük olmalı

Price__c <= 1000
Hata Mesajı: "Fiyat 1000 TL'den büyük olmalıdır."

#13. Discount yüzde 50'den fazla olamaz (Opportunity)

Discount__c > 50
Hata Mesajı: "İndirim %50'den fazla olamaz."

#14. Account oluştururken Account Number alfabetik olamaz

REGEX(AccountNumber, ".*[A-Za-z]+.*")
Hata Mesajı: "Hesap numarası sadece rakam içermelidir."

# 15. Tedarikçi seçildiğinde Tedarikçi Kodu zorunlu olmalı

AND(
Checkbox_Is_Supplier__c = TRUE,
ISBLANK(Supplier_Code__c)
)
Hata Mesajı: "Tedarikçi kodu girilmelidir."

#16. Ödeme tarihi, fatura tarihinden önce olamaz

Payment_Date__c < Invoice_Date__c
Hata Mesajı: "Ödeme tarihi, fatura tarihinden önce olamaz."

# 17. Lead kaynağı boş olamaz

ISBLANK(LeadSource)
Hata Mesajı: "Lead kaynağı belirtilmelidir."

# 18. Email alanında boşluk varsa hata ver

CONTAINS(Email, " ")
Hata Mesajı: "E-posta adresinde boşluk olamaz."

#19. Görev (Task) tarihi geçmişte olamaz

ActivityDate < TODAY()
Hata Mesajı: "Görev tarihi geçmişte olamaz."

# 20. Müşteri notu 250 karakterden uzun olamaz

LEN(Customer_Notes__c) > 250
Hata Mesajı: "Müşteri notu en fazla 250 karakter olabilir."