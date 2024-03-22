.. role:: python(code)
   :language: python

Schemat uzycia IMAP
===================

.. code-block:: python
   :emphasize-lines: 10, 16
   :linenos:

   import email
   import imaplib

   imap_ssl = imaplib.IMAP4_SSL(host="imap.gmail.com", port=993)

   resp_code, response = imap_ssl.login("someuser@gmail.com", app_password)  # Response jest jednoelementową listą

   resp_code, mail_count = imap_ssl.select(mailbox="INBOX", readonly=True) # OK [b'62']

   resp_code, mail_ids = imap_ssl.search(None, "ALL") # resp-code: OK, mail-ids: [b'1 2 3 4 5 6 7 8 9 10 ...']
   ids = mail_ids[0].decode().split() # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ...]

   for mail_id in ids[-2]:
       print("================== Start of Mail [{}] ====================".format(mail_id))

       resp_code, mail_data = imap_ssl.fetch(mail_id, '(RFC822)')  # # Fetch mail data.
       # OK [(b'62 (RFC822 {16141}', b'Delivered-To: leszekimielski@gmail.com\r\nReceived: by 2002:a05:6a10:8 ...]

       message = email.message_from_bytes(mail_data[0][1])  # # Construct Message from mail data
       print("From       : {}".format(message.get("From")))
       print("To         : {}".format(message.get("To")))
       print("Bcc        : {}".format(message.get("Bcc")))
       print("Date       : {}".format(message.get("Date")))
       print("Subject    : {}".format(message.get("Subject")))

       print("Body : ")
       for part in message.walk():
           if part.get_content_type() == "text/plain":
               body_lines = part.as_string().split("\n")
               print("\n".join(body_lines[:12]))  # ## Print first 12 lines of message

       print("================== End of Mail [{}] ====================\n".format(mail_id))

   # ############ Close Selected Mailbox #######################
   imap_ssl.close()


Ten fragment kodu odpowiada za odpowiednie połączenie z serwerem pocztowym przez IMAP i pobranie listy wiadomości e-mail z wybranego folderu poczty. Spróbuję to wytłumaczyć krok po kroku.

:python:`imap_ssl = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)`

Ta linia tworzy nowe połączenie do serwera IMAP. Jest to serwer poczty, który przechowuje wiadomości e-mail na serwerze i pozwala klientom na ich pobieranie.
IMAP4_SSL jest wersją protokołu IMAP, która używa SSL (Secure Sockets Layer) do zapewnienia bezpiecznej komunikacji.

:python:`imap_ssl.login(USERNAME, PASSWORD)`

Ta linia loguje się na serwer IMAP za pomocą podanej nazwy użytkownika i hasła.

:python:`imap_ssl.select('INBOX')`

Ta linia wybiera skrzynkę odbiorczą (INBOX) do pracy.
Możesz wybrać inne skrzynki, takie jak wysłane e-maile (SENT), ale w tym przypadku pracujemy na skrzynce odbiorczej.

:python:`resp_code, mail_ids = imap_ssl.search(None, "ALL")`

zwraca odpowiedż w formie :python:`'OK'` oraz :python:`mail_ids` -- jednolelementową listę binarnych danych odzielanych spacjami, przedstawiającymi numery sekwencyjne wiadomosci e-mail

Następnie w celu uzyskania informacji o wiadomosci takich jak ngłówki i treść używamy metody :python:`fetch(mail_id, 'RFC822`)
Inne mozliwości zamiast RFC822 to:
:python:`resp_code` zwraca :python`'OK'` bądź ..
natomiast :python:`mail_data` to lista zawierająca dane na temat wiadomości, czyli numeru sekwencyjnego maila, danych, ktore sa przesylane, dlugości meila w byte'ach, oraz nagłówka, treści wiadomości i załaczników

:python:`mail_data = [ (TUPLA), b')']`

Czyli :python:`mail_data` ma strukturę listy jednoelementowej w ktorej element jest tuplą :python:`((TUPLA), b')')`

:python:`TUPLA = (b'numer_sekwencyjny (RFC822 {ilość byte\`ów}\', Nagłówek oraz treść i załączniki)`

albo inaczej

:python:`TUPLA[0] = b'numer_sekwencyjny (RFC822 {ilość byte\`ów}\'`
:python:`TUPLA[1] = Nagłówek oraz treść i załączniki`

i na koniec wynika z tego, że

:python:`mail_data[0][0]` odnosi się do :python:`b'numer_sekwencyjny (RFC822 {ilość byte\`ów}\'

:python:`mail_data[0][1]` odnosi się do **Nagłówka oraz treści i załączników**

Z uzyciem uid()
---------------

aby uzywać uid zmiast numerow sekwencji

# Zamiast pobierania numerów sekwencji nalezy pobierać uid.
W tym celu należy w kodzie prezentowanym wyżej zastosować nastepujące zmiany

.. code-block::
   :linenos:

   resp_code, mail_ids = imap_ssl.search(None, "ALL")
   ids = mail_ids[0].decode().split()
   # Użyj:
   resp_code, uids_data = imap_ssl.uid('search', None, 'ALL')
   uids = uids_data[0].split()

oraz zamiast uzywać mail_id do pobierania maili nalezy uzyć uid

.. code-block::
   :linenos:

   # Zamiast:
   resp_code, mail_data = imap_ssl.fetch(mail_id, '(RFC822)') # Fetch mail data.
   # Użyj:
   resp_code, mail_data = imap_ssl.uid('fetch', uid, '(RFC822)') # Fetch mail data using UID.


Tak więc dla jasności nasz cały kod z uzyciem uid bedzie wygladał nastepująco

.. code-block:: python
   :emphasize-lines: 10, 16
   :linenos:

   import imaplib
   import email

   imap_ssl = imaplib.IMAP4_SSL(host="imap.gmail.com", port=993)

   resp_code, response = imap_ssl.login("someuser@gmail.com", "app_password")

   resp_code, mail_count = imap_ssl.select(mailbox="ELITMUS", readonly=True)

   resp_code, uids_data = imap_ssl.uid('search', None, 'ALL')
   uids = uids_data[0].split()

   for uid in uids[-2:]:
       print("================== Start of Mail [{}] ====================".format(uid))

       resp_code, mail_data = imap_ssl.uid('fetch', uid, '(RFC822)') ## Fetch mail data using UID.

       message = email.message_from_bytes(mail_data[0][1]) ## Construct Message from mail data
       print("From       : {}".format(message.get("From")))
       print("To         : {}".format(message.get("To")))
       print("Bcc        : {}".format(message.get("Bcc")))
       print("Date       : {}".format(message.get("Date")))
       print("Subject    : {}".format(message.get("Subject")))

       print("Body : ")
       for part in message.walk():
           if part.get_content_type() == "text/plain":
               body_lines = part.as_string().split("\n")
               print("\n".join(body_lines[:12])) ### Print first 12 lines of message

       print("================== End of Mail [{}] ====================\n".format(uid))

   imap_ssl.close()




Ta linia wyszukuje wszystkie e-maile w bieżącej skrzynce pocztowej.

- 'search' to polecenie IMAP używane do wyszukiwania wiadomości spełniających określone kryteria - w tym wypadku,
- "ALL" oznacza, że szukamy wszystkich wiadomości.
- uid to metoda używana do wysyłania poleceń, które operują na konkretnych wiadomościach. Zwraca dwa elementy: status operacji (result) i dane (data). Dane zawierają listę identyfikatorów unikalnych wiadomości, które pasują do kryteriów wyszukiwania.


Różnica między pobieraniem wiadomości za pomocą identyfikatorów UID a numerów sekwencyjnych polega na tym, że używamy różnych poleceń w protokole IMAP.

Kiedy pracujemy z identyfikatorami UID, używamy polecenia UID FETCH. Aby wykonać to polecenie w bibliotece IMAP dla Pythona, korzystamy z metody uid(). Natomiast kiedy pracujemy z numerami sekwencyjnymi, używamy po prostu polecenia FETCH.

W związku z tym, gdy operujemy na numerach UID, stosujemy metodę uid() z odpowiednimi argumentami, aby pobrać dane wiadomości za pomocą polecenia UID FETCH, a gdy operujemy na numerach sekwencyjnych, stosujemy metodę fetch() z odpowiednimi argumentami, aby pobrać dane wiadomości za pomocą polecenia FETCH.


Sprawdzić czy kody są poprawne

.. code-block::
   :linenos:

   # Wyszukaj wiadomości w skrzynce pocztowej na podstawie numerów UID

   # Zakres numerów UID wiadomości
   uid_range = '1:5'

   # Wykonaj wyszukiwanie
   resp_code, matching_uids = imap_ssl.search(None, 'UID', uid_range)

   # Sprawdź kod odpowiedzi i znalezione identyfikatory wiadomości
   print("Kod odpowiedzi:", resp_code)
   print("Znalezione identyfikatory UID wiadomości:", matching_uids)


.. code-block::
   :linenos:

   # Wyszukaj wiadomości w skrzynce pocztowej na podstawie numerów sekwencyjnych (mail_id)

   # Zakres numerów sekwencyjnych wiadomości
   mail_id_range = '1:5'

   # Wykonaj wyszukiwanie
   resp_code, matching_ids = imap_ssl.search(None, 'SEQUENCE', mail_id_range)

   # Sprawdź kod odpowiedzi i znalezione identyfikatory wiadomości
   print("Kod odpowiedzi:", resp_code)
   print("Znalezione identyfikatory wiadomości:", matching_ids)
