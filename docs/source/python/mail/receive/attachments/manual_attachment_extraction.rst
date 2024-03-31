Ręczne Pobieranie załączników
=============================

.. code-block:: python
   :linenos:

   import imaplib
   import email
   import os

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
       for part in msg.get_payload():
           if part.get_content_maintype() == 'multipart':
               # Pomijanie części typu multipart
               continue

           # Sprawdzanie nagłówka Content-Disposition, aby zidentyfikować załączniki
           disposition = part.get('Content-Disposition')
           if disposition and disposition.startswith('attachment'):
               # Pobieranie nazwy załącznika
               filename = part.get_filename()

               # Pobieranie treści załącznika
               attachment_data = part.get_payload(decode=True)

               # Zapisywanie załącznika na dysku
               with open(filename, 'wb') as f:
                   f.write(attachment_data)

   # Zamykanie połączenia
   mail.logout()

Poprawnie zidentyfikowane nagłówki dla jednego załącznika powinny zawierać przynajmniej dwa kluczowe nagłówki:

1. `Content-Disposition`: Określa, jak klient poczty e-mail powinien obsługiwać załącznik.
   Nagłówek ten informuje, że załącznik jest dołączany do wiadomości. W tym nagłówku należy podać również nazwę pliku załącznika.

```python
image_part.add_header('Content-Disposition', 'attachment', filename='obrazek.jpg')
```

2. `Content-Transfer-Encoding`: Określa sposób kodowania zawartości załącznika. W przypadku załączników,
często stosuje się kodowanie base64, aby przekazywać binarne dane w postaci tekstu.

```python
image_part.add_header('Content-Transfer-Encoding', 'base64')
```

Dodatkowe nagłówki mogą być również używane w zależności od potrzeb i specyfiki załącznika, takie jak `Content-Type`
do określenia typu MIME załącznika, lub `Content-ID` dla identyfikacji w treści powiązanej. Jednakże,
w kontekście minimalnej konfiguracji, `Content-Disposition` i `Content-Transfer-Encoding` są najważniejsze.

Rozkodowywanie
--------------

Aby rozkodować załącznik, musimy znać sposób jego zakodowania. W większości przypadków załączniki są kodowane
w formacie base64 lub quoted-printable. Możemy sprawdzić to na podstawie nagłówka `Content-Transfer-Encoding`
dla danej części wiadomości.

Oto jak możemy sprawdzić sposób kodowania i rozkodować załącznik bez korzystania z funkcji `walk()`:

.. code-block:: python
   :linenos:

   import imaplib
   import email
   import base64
   from email.header import decode_header

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
       for part in msg.get_payload():
           if part.get_content_maintype() == 'multipart':
               continue

           # Sprawdzanie nagłówka Content-Disposition, aby zidentyfikować załączniki
           disposition = part.get('Content-Disposition')
           if disposition and disposition.startswith('attachment'):
               # Pobieranie nazwy załącznika
               filename = part.get_filename()

               # Sprawdzanie nagłówka Content-Transfer-Encoding
               encoding = part.get('Content-Transfer-Encoding', '').lower()

               # Pobieranie treści załącznika
               attachment_data = part.get_payload(decode=True)

               # Rozkodowywanie załącznika, jeśli jest zakodowany
               if encoding == 'base64':
                   attachment_data = base64.b64decode(attachment_data)

               # Zapisywanie załącznika na dysku
               with open(filename, 'wb') as f:
                   f.write(attachment_data)

   # Zamykanie połączenia
   mail.logout()


Jeśli załącznik jest kodowany w sposób inny niż base64, musimy zaimplementować odpowiednie procedury
dekodowania dla danego rodzaju kodowania.

Oto jak możemy obsłużyć różne typy kodowania załącznika:

.. code-block:: python
   :linenos:

   import imaplib
   import email
   import base64
   import quopri  # Do obsługi quoted-printable
   from email.header import decode_header

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
       for part in msg.get_payload():
           if part.get_content_maintype() == 'multipart':
               continue

           # Sprawdzanie nagłówka Content-Disposition, aby zidentyfikować załączniki
           disposition = part.get('Content-Disposition')
           if disposition and disposition.startswith('attachment'):
               # Pobieranie nazwy załącznika
               filename = part.get_filename()

               # Sprawdzanie nagłówka Content-Transfer-Encoding
               encoding = part.get('Content-Transfer-Encoding', '').lower()

               # Pobieranie treści załącznika
               attachment_data = part.get_payload(decode=True)

               # Rozkodowywanie załącznika, jeśli jest zakodowany
               if encoding == 'base64':
                   attachment_data = base64.b64decode(attachment_data)
               elif encoding == 'quoted-printable':
                   attachment_data = quopri.decodestring(attachment_data)

               # Zapisywanie załącznika na dysku
               with open(filename, 'wb') as f:
                   f.write(attachment_data)

   # Zamykanie połączenia
   mail.logout()


W tym kodzie dodano obsługę kodowania "quoted-printable" za pomocą modułu `quopri`, który jest używany do dekodowania
danych w tym formacie. Jeśli załącznik jest kodowany w innym formacie, trzeba byłoby użyć odpowiednich procedur
dekodowania dla tego konkretnego typu kodowania.

W tym kodzie, po znalezieniu załącznika, sprawdzamy nagłówek `Content-Transfer-Encoding`, aby ustalić, czy załącznik
jest zakodowany. Jeśli jest zakodowany w formacie base64, używamy funkcji `base64.b64decode()` do jego rozkodowania
przed zapisaniem na dysku.

Inne kodowania
~~~~~~~~~~~~~~

Aby zgeneralizować obsługę różnych rodzajów kodowania załączników, można stworzyć funkcję, która będzie a
utomatycznie dobierała odpowiednią procedurę dekodowania na podstawie wartości nagłówka `Content-Transfer-Encoding`.
Poniżej przedstawiono przykładową funkcję, która realizuje ten cel:

.. code-block:: python
   :linenos:

   import base64
   import quopri

   def decode_attachment(attachment_data, encoding):
       """
       Dekoduje zawartość załącznika na podstawie podanego kodowania.

       :param attachment_data: Dane załącznika do dekodowania.
       :param encoding: Kodowanie załącznika (np. 'base64' lub 'quoted-printable').
       :return: Rozkodowane dane załącznika.
       """
       if encoding == 'base64':
           return base64.b64decode(attachment_data)
       elif encoding == 'quoted-printable':
           return quopri.decodestring(attachment_data)
       else:
           # Obsługa innych typów kodowania, jeśli wymagane
           # Tutaj można dodać obsługę innych kodowań, jeśli jest to potrzebne
           # Na przykład, można obsłużyć kodowanie 'uuencode', '7bit', '8bit', itp.
           # Jeśli nie można znaleźć odpowiedniego kodowania, można zwrócić oryginalne dane
           return attachment_data

   # Przykład użycia funkcji
   attachment_data = b'TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlz\nIGtleSBz'  # Załącznik zakodowany w base64
   encoding = 'base64'

   decoded_data = decode_attachment(attachment_data, encoding)
   print(decoded_data)


W tej funkcji `decode_attachment()` przyjmuje dane załącznika do dekodowania oraz kodowanie załącznika.
Następnie na podstawie wartości kodowania, funkcja dekoduje dane załącznika przy użyciu odpowiedniej
procedury dekodowania (np. `base64.b64decode()` dla kodowania base64 lub `quopri.decodestring()`
dla kodowania quoted-printable).

Jeśli załącznik jest kodowany w innym formacie, można dodać obsługę tego kodowania do funkcji,
w celu uwzględnienia innych możliwych typów kodowania. Funkcja może być łatwo rozbudowana,
aby obsługiwać różne scenariusze kodowania załączników.
