Fnnkcje
=======

sendmail()
----------

:python:`sendmail('sender@adres.email, receiver@adres.email, msg)`

Wartością zwrotną metody sendmail() jest słownik. W słowniku będzie umiesz- czona para klucz-wartość dla każdego
odbiorcy, do którego nie udało się dostarczyć wiadomości e-mail.
Dlatego też pusty słownik oznacza, że udało się dostarczyć tę wiadomość wszystkim odbiorcom.

msg, czyli ciąg tekstowy treści wiadomości musi rozpoczynać się od :python:`'Subject: \n'`
