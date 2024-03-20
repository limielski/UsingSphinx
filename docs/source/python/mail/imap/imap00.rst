Wstęp: Algorytm połączenia
==========================

.. code-block:: python
   :linenos:

   mail = imaplib.IMAP4_SSL(IMAP_SERVER)
   mail.login(USERNAME, PASSWORD)

   # Select the mailbox you want to delete in
   mail.select("INBOX")

   # Get the list of emails
   result = ''
   data = []
   if mail is not None:
       result, data = mail.uid('search', None, "ALL")
   else:
       print('Failed to connect to the mail server.')

Ten fragment kodu odpowiada za odpowiednie połączenie z serwerem pocztowym przez IMAP i pobranie listy wiadomości e-mail z wybranego folderu poczty. Spróbuję to wytłumaczyć krok po kroku.

mail = imaplib.IMAP4_SSL(IMAP_SERVER):

Ta linia tworzy nowe połączenie do serwera IMAP. Jest to serwer poczty, który przechowuje wiadomości e-mail na serwerze i pozwala klientom na ich pobieranie.
IMAP4_SSL jest wersją protokołu IMAP, która używa SSL (Secure Sockets Layer) do zapewnienia bezpiecznej komunikacji.

mail.login(USERNAME, PASSWORD):

Ta linia loguje się na serwer IMAP za pomocą podanej nazwy użytkownika i hasła.

mail.select('INBOX'):

Ta linia wybiera skrzynkę odbiorczą (INBOX) do pracy.
Możesz wybrać inne skrzynki, takie jak wysłane e-maile (SENT), ale w tym przypadku pracujemy na skrzynce odbiorczej.

result, data = mail.uid('search', None, "ALL"):

Ta linia wyszukuje wszystkie e-maile w bieżącej skrzynce pocztowej.

- 'search' to polecenie IMAP używane do wyszukiwania wiadomości spełniających określone kryteria - w tym wypadku,
- "ALL" oznacza, że szukamy wszystkich wiadomości.
- uid to metoda używana do wysyłania poleceń, które operują na konkretnych wiadomościach. Zwraca dwa elementy: status operacji (result) i dane (data). Dane zawierają listę identyfikatorów unikalnych wiadomości, które pasują do kryteriów wyszukiwania.
