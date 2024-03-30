Metoda walk() - Pobieranie załaczników
======================================

Automatyczne pobieranie załączników polega na wykorzystaniu funkcji :python:`walk()` do rekurencyjnego przeszukiwania treści
wiadomości e-mail i automatycznego identyfikowania oraz pobierania załączników. Ten proces eliminuje konieczność
ręcznej analizy części wiadomości i nagłówków, ponieważ funkcja walk() iteruje przez wszystkie części wiadomości,
włączając w to zagnieżdżone treści multipart, aby zlokalizować załączniki na podstawie ich nagłówków MIME. Automatyczne
pobieranie załączników upraszcza proces pobierania załączników z wiadomości e-mail i jest szczególnie przydatne do
obsługi wiadomości o złożonej strukturze lub zawierających wiele załączników.

Poniżej znajduje się zmodyfikowany kod, który uwzględnia różne kodowania załączników i odpowiednio je dekoduje:

.. code-block:: Python
   :linenos:

   import imaplib
   import email
   import os
   import base64
   import quopri

   # Dane do połączenia z serwerem IMAP
   IMAP_SERVER = 'imap.example.com'
   EMAIL = 'your_email@example.com'
   PASSWORD = 'your_password'

   # Tworzenie połączenia z serwerem IMAP
   mail = imaplib.IMAP4_SSL(IMAP_SERVER)
   mail.login(EMAIL, PASSWORD)

   # Wybór skrzynki pocztowej
   mail.select('INBOX')

   # Wyszukiwanie wiadomości
   status, messages = mail.search(None, 'ALL')
   messages = messages[0].split()

   for msg_id in messages:
       # Pobieranie treści wiadomości
       status, data = mail.fetch(msg_id, '(RFC822)')
       raw_email = data[0][1]

       # Parsowanie wiadomości e-mail
       msg = email.message_from_bytes(raw_email)

       # Sprawdzanie załączników
       for part in msg.walk():
           if part.get_content_maintype() == 'multipart':
               continue
           if part.get('Content-Disposition') is None:
               continue

           # Sprawdzanie nagłówka Content-Disposition, aby zidentyfikować załączniki
           disposition = part.get('Content-Disposition')
           if disposition.startswith('attachment'):
               # Pobieranie nazwy załącznika
               filename = part.get_filename()

               # Pobieranie kodowania załącznika
               encoding = part.get('Content-Transfer-Encoding', '').lower()

               # Pobieranie treści załącznika
               attachment_data = part.get_payload(decode=True)

               # Dekodowanie załącznika, jeśli jest zakodowany
               if encoding == 'base64':
                   attachment_data = base64.b64decode(attachment_data)
               elif encoding == 'quoted-printable':
                   attachment_data = quopri.decodestring(attachment_data)

               # Zapisywanie załącznika na dysku
               with open(filename, 'wb') as f:
                   f.write(attachment_data)

   # Zamykanie połączenia
   mail.logout()


W tym kodzie dodano obsługę różnych kodowań załączników. Jeśli załącznik jest zakodowany w formacie base64, używana jest funkcja `base64.b64decode()` do jego dekodowania. Natomiast jeśli jest zakodowany w formacie quoted-printable, używana jest funkcja `quopri.decodestring()` do jego dekodowania. Dzięki temu kod jest w stanie prawidłowo obsługiwać różne rodzaje kodowania załączników.

Inne metody kodowania
---------------------

Oprócz kodowania base64 i quoted-printable, istnieją inne metody kodowania, które mogą być potencjalnie używane
dla załączników w wiadomościach e-mail. Kilka z nich to:

1. **UUEncode**: Jest to metoda kodowania często używana do zamieniania danych binarnych na formę tekstową,
która jest bezpieczna do przesyłania w wiadomościach e-mail. Dzięki temu może być używana jako sposób kodowania załączników.

2. **7bit**: Jest to prosty format, który może przechowywać tylko znaki ASCII w postaci 7-bitowej, co oznacza,
że jest on odpowiedni do przechowywania tekstu, ale nie obsługuje danych binarnych. Jednakże, w niektórych przypadkach,
załączniki mogą być kodowane jako 7-bitowe dane.

3. **8bit**: Podobnie jak 7bit, jest to format, który może przechowywać znaki ASCII, ale może również obsługiwać znaki
spoza zakresu ASCII. Jednakże, podobnie jak 7bit, 8bit nie jest odpowiedni do kodowania danych binarnych.

4. **binary (binhex)**: Binhex to metoda kodowania, która jest stosowana głównie w środowiskach Macintosh.
Polega ona na przekształceniu danych binarnych w formę tekstową, która jest bezpieczna do przesyłania przez e-mail.

5. **x-uuencode**: Jest to rozszerzenie metody UUEncode, które może być używane do kodowania danych binarnych
w formie tekstowej.

Oczywiście istnieją inne metody kodowania, ale te są najczęściej spotykane w kontekście załączników w wiadomościach
e-mail. Ważne jest, aby kod był elastyczny i mógł obsługiwać różne rodzaje kodowania,
które mogą być używane w danych wiadomościach.
