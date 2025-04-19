""" #1. Contact Oluşturulunca Account Adı Kopyala

trigger CopyAccountName on Contact (before insert) {
    for(Contact c : Trigger.new){
        if(c.AccountId != null){
            Account acc = [SELECT Name FROM Account WHERE Id = :c.AccountId];
            c.Description = 'Related Account: ' + acc.Name;
        }
    }
}
# 2. Account Oluşunca Otomatik Numara Ver

trigger AutoNumberAccount on Account (before insert) {
    Integer counter = 1000;
    for(Account acc : Trigger.new){
        acc.AccountNumber = 'ACC-' + counter++;
    }
}
# 3. Contact Güncellenince Status Güncelle

trigger UpdateContactStatus on Contact (before update) {
    for(Contact c : Trigger.new){
        if(c.Email != Trigger.oldMap.get(c.Id).Email){
            c.Status__c = 'Email Changed';
        }
    }
}
# 4. Lead Silinmeden Önce Log Tut

trigger LogLeadDelete on Lead (before delete) {
    for(Lead l : Trigger.old){
        System.debug('Deleted Lead: ' + l.Name);
    }
}
🏷# 5. Opportunity Kaydedilince Stage Logla

trigger LogOpportunityStage on Opportunity (after insert) {
    for(Opportunity opp : Trigger.new){
        System.debug('Stage: ' + opp.StageName);
    }
}
# 6. Custom Object Değişince Related Object Güncelle

trigger UpdateRelatedCustom on Custom_Object__c (after update) {
    for(Custom_Object__c c : Trigger.new){
        Related_Object__c r = [SELECT Name FROM Related_Object__c WHERE Id = :c.Related_Id__c];
        r.Status__c = 'Updated by Trigger';
        update r;
    }
}
#7. Task Oluşunca Tarihi Kontrol Et

trigger ValidateTaskDate on Task (before insert) {
    for(Task t : Trigger.new){
        if(t.ActivityDate < Date.today()){
            t.addError('Task date cannot be in the past!');
        }
    }
}
# 8. Case Kapatılınca Log Yaz

trigger CaseCloseLogger on Case (after update) {
    for(Case c : Trigger.new){
        if(c.Status == 'Closed' && Trigger.oldMap.get(c.Id).Status != 'Closed'){
            System.debug('Case closed: ' + c.Id);
        }
    }
}
# 9. Her Yeni Record’a UUID Ata

trigger AssignUUID on Account (before insert) {
    for(Account acc : Trigger.new){
        acc.Custom_UUID__c = String.valueOf(Math.random()).substring(2, 12);
    }
}
# 10. Opportunity Fırsat Tutarı Değiştiyse Bildir

trigger NotifyOpportunityAmountChange on Opportunity (after update) {
    for(Opportunity o : Trigger.new){
        if(o.Amount != Trigger.oldMap.get(o.Id).Amount){
            System.debug('Amount changed on opportunity: ' + o.Id);
        }
    }
}
# 11. Product Eklenince Quantity Kontrolü

trigger ValidateProductQuantity on OpportunityLineItem (before insert) {
    for(OpportunityLineItem item : Trigger.new){
        if(item.Quantity <= 0){
            item.addError('Quantity must be greater than 0');
        }
    }
}
# 12. Lead to Contact Dönüşümünde Not Aktarımı

trigger CopyNotesOnConversion on Lead (after update) {
    for(Lead l : Trigger.new){
        if(l.IsConverted){
            Contact c = [SELECT Id FROM Contact WHERE Id = :l.ConvertedContactId];
            c.Description = l.Description;
            update c;
        }
    }
}
# 13. Kullanıcı Profili Admin Değilse Kısıtla

trigger RestrictDeleteAccount on Account (before delete) {
    if(UserInfo.getProfileId() != '00eXXXXXXXXXXXX'){
        for(Account a : Trigger.old){
            a.addError('You are not authorized to delete Accounts');
        }
    }
}
# 14. Aynı İsimli Contact'ı Engelle

trigger PreventDuplicateContact on Contact (before insert) {
    for(Contact c : Trigger.new){
        List<Contact> existing = [SELECT Id FROM Contact WHERE FirstName = :c.FirstName AND LastName = :c.LastName];
        if(!existing.isEmpty()){
            c.addError('Duplicate Contact Detected');
        }
    }
}
# 15. Telefon Formatı Doğrulama

trigger ValidatePhoneFormat on Contact (before insert) {
    for(Contact c : Trigger.new){
        if(!Pattern.matches('\\(\\d{3}\\) \\d{3}-\\d{4}', c.Phone)){
            c.addError('Phone must be in format (123) 456-7890');
        }
    }
}
# 16. Contact Sayısını Say ve Account’a Yaz

trigger CountContacts on Contact (after insert, after delete) {
    Set<Id> accountIds = new Set<Id>();
    for(Contact c : Trigger.isInsert ? Trigger.new : Trigger.old){
        accountIds.add(c.AccountId);
    }
    List<Account> accounts = [SELECT Id, Contact_Count__c, (SELECT Id FROM Contacts) FROM Account WHERE Id IN :accountIds];
    for(Account a : accounts){
        a.Contact_Count__c = a.Contacts.size();
    }
    update accounts;
}
# 17. Önceden Tanımlı Alanları Otomatik Doldur

trigger DefaultFieldValues on Account (before insert) {
    for(Account a : Trigger.new){
        if(a.Industry == null){
            a.Industry = 'Technology';
        }
    }
}
# 18. Parent Account Bilgisini Child Account’a Yaz

trigger CopyParentAccountInfo on Account (before insert) {
    for(Account a : Trigger.new){
        if(a.ParentId != null){
            Account parent = [SELECT Name FROM Account WHERE Id = :a.ParentId];
            a.Description = 'Parent Account: ' + parent.Name;
        }
    }
}
# 19. Team Member Eklenince Email Gönder

trigger NotifyTeamAddition on AccountTeamMember (after insert) {
    for(AccountTeamMember tm : Trigger.new){
        Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();
        mail.setSubject('New Team Member Added');
        mail.setPlainTextBody('A new team member was added to account: ' + tm.AccountId);
        mail.setToAddresses(new String[]{'admin@example.com'});
        Messaging.sendEmail(new Messaging.SingleEmailMessage[]{mail});
    }
}
# 20. After Trigger ile Async İşlem Başlatma

trigger AsyncTriggerExample on Account (after insert) {
    MyAsyncJobClass.runAsync(Trigger.newMap.keySet());
}"""