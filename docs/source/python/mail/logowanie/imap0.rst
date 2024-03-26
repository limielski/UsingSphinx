Logowanie imap
==============


.. code-block:: python
   :emphasize-lines: 8
   :linenos:

   import imaplib

   IMAP_SERVER = 'imap.example.com'
   IMAP_PORT = 993
   USERNAME = 'your_username'
   PASSWORD = 'your_password'

   mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
   mail.login(USERNAME, PASSWORD)

   # Wykonanie operacji na skrzynce pocztowej
   # np. pobranie listy folderów, pobranie wiadomości, itp.

   # Zamknięcie połączenia
   imap_connection.logout()


funkcja :python:`imaplib.IMAP4_SSL(host, port)`
służy do nawiązywania bezpiecznego połączenia z serwerem IMAP przez protokół SSL/TLS. IMAP (Internet Message Access Protocol) jest protokołem używanym do pobierania wiadomości e-mail z serwera. Bezpieczne połączenie za pomocą SSL/TLS zapewnia szyfrowanie komunikacji między klientem a serwerem, co chroni poufne dane, takie jak hasła i treści wiadomości e-mail, przed przechwyceniem przez osoby trzecie.

Funkcja **imaplib.IMAP4_SSL** tworzy obiekt klienta IMAP, który może być używany do komunikacji z serwerem IMAP. Przyjmuje ona jeden argument opcjonalny, którym jest nazwa hosta serwera IMAP. Jeśli nie podano nazwy hosta, funkcja imaplib.IMAP4_SSL zwróci błąd, ponieważ wymaga ona określenia, z którym serwerem IMAP należy się połączyć.
Do połączenia domyslnie stosowany jest port 993

W tym przykładzie:

* tworzymy obiekt imap_connection poprzez wywołanie funkcji :python:`imaplib.IMAP4_SSL('mail.example.com')` , gdzie \'mail.example.com\' jest adresem hosta serwera IMAP.
* Następnie autoryzujemy się na serwerze poprzez metodę login, używając nazwy użytkownika i hasła.
* Po zakończeniu operacji na skrzynce pocztowej zaleca się zamknięcie połączenia za pomocą metody logout.
