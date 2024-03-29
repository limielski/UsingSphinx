Jak wysyłac załączniki
======================

W ostatnim artykule omówiliśmy podstawy wysyłania wiadomości e-mail z konta Gmail bez tematu i bez załącznika.
Dzisiaj dowiemy się, jak wysyłać pocztę z załącznikiem i tematem za pomocą Pythona.
Zanim przejdziesz dalej, zdecydowanie zaleca się nauczenie się wysyłania prostych wiadomości e-mail za pomocą
języka Python i poznanie podstaw działania biblioteki „smtplib” w języku Python.

Jeśli przeczytałeś poprzedni artykuł, zdobyłeś wiedzę jak powstaje sesja i jak ona działa.
Teraz musisz nauczyć się dołączać plik i temat do wiadomości e-mail.
W tym celu musisz zaimportować niektóre natywne biblioteki Pythona.
Z tych bibliotek należy zaimportować narzędzia używane w naszych programach.

Kroki, aby wysłać pocztę z załącznikami z konta Gmail:

1. Aby dodać załącznik należy zaimportować:

 - :python:`smtplib`
 - :python:`from email.mime.multipart import MIMEMultipart`
 - :python:`from email.mime.text import MIMEText`
 - :python:`from email.mime.base import MIMEBase`
 - :python:`from email import encoders`

   To kilka bibliotek, które ułatwią nam pracę.
   Są to biblioteki natywne i nie trzeba w tym celu importować żadnej biblioteki zewnętrznej.


2. Utwórz instancję :python:`msg = MIMEMultipart()`

   .. note:: argumentami :python:`MIMEMultipart()` są:

      - 'alternative'
      - 'mixed'
      - 'related'
      - 'digest'
      - 'report'
      - 'signed'
      - 'encrypted'
      - 'form-data'
      - 'x-mixed-replace'
      - 'byterange'

      Zobacz:

      - `MIME Wikipedia pl <https://pl.wikipedia.org/wiki/Multipurpose_Internet_Mail_Extensions>`_
      - `MIME wikipedia en: <https://en.wikipedia.org/wiki/MIME>`_



3. Podaj dane nadawcy, odbiorcy, temat ...

 - :python:`msg['From' = adress_from`
 - :python:`msg['To' = adress_from`
 - :python:`msg['Subject' = adress_from`

4. W ciagu znakow podaj treść listu i dołącz ją do załącznika

 - :python:`body = "Body of te mail"`
 - :python:`msg.attach(MIMEText(body, 'plain'))`

.. note:: W przypadku dołaczania html, jesli sa dodatkowe obrazki pliki dołaczane do html, trzeba to zrobic
   troche inaczej - :ref:`zobacz jak <HTMLzobrazkiem>`

5. Otwórz plik, który chcesz dołączyć w trybie 'rb', nastepnie utwórz instancję MIMEBase z dwoma parametrami.
Pierwszy to `_maintype` na przykład 'text', 'image', a drugi to `_subtype` np. 'gif', 'jpg' ... .
Jest to klasa mazowa dla wszystkich podklas Message specyficznych dla MIME

 - :python:`filename = "file_name_with_extension"`
 - :python:`attachment = open(filename, 'rb')`
 - :python:`p = MIMEBase(application, 'octet_stream')`

6. Funkcja :python:`set_payload` jest używana do zmiany treści na postać zakodowaną.
Należy zakodować ją za pomocą `encode_base64`. Na koniec dodaj nagłówek i załącz plik do instancji `MIMEMultipart`
utworzonej wiadomości `msg`. Zakoduj go w `encode_base64` i dołącz plik z utworzoną instancją `MIMEMultipart` msg.

 - :python:`p.set_payload((attachment).read())`
 - :python:`encoders.encode_base64(p)`
 - :python:`p.add_header('Content-Disposition', "attachment; filename= %s" % filename)`
 - :python:`msg.attach(p)`

.. note:: Jeżeli używamy załącznik za pomocą MIMEImage, bądź MIMEText, to nie musimy uzywać set_payload

7. Po wykonaniu tych kroków postępuj zgodnie z instrukcjami opisanymi w poprzednim artykule,
aby utworzyć sesję, zabezpieczyć ją i sprawdzić autentyczność,  przeslij wiadomość, konwertując msg na string.
Nnastępnie po wysłaniu wiadomości zakończyć sesję.

 - :python:`s = smtplib.SMTP('smtp.gmail.com', 587)`
 - :python:`s.starttls()`
 - :python:`s.login(fromaddr, "Password_of_the_sender")`
 - :python:`text = msg.as_string() # Converts the Multipart msg into a string`
 - :python:`s.sendmail(fromaddr, toaddr, text)`
 - :python:`s.quit() # terminating the session`
