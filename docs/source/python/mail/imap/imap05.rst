Opis funkcji
============

imaplib.IMAP4_SSL
-----------------

służy do nawiązywania bezpiecznego połączenia z serwerem IMAP przez protokół SSL/TLS. IMAP (Internet Message Access Protocol) jest protokołem używanym do pobierania wiadomości e-mail z serwera. Bezpieczne połączenie za pomocą SSL/TLS zapewnia szyfrowanie komunikacji między klientem a serwerem, co chroni poufne dane, takie jak hasła i treści wiadomości e-mail, przed przechwyceniem przez osoby trzecie.

Funkcja **imaplib.IMAP4_SSL** tworzy obiekt klienta IMAP, który może być używany do komunikacji z serwerem IMAP. Przyjmuje ona jeden argument opcjonalny, którym jest nazwa hosta serwera IMAP. Jeśli ta nazwa nie jest podana, funkcja spróbuje nawiązać połączenie z serwerem IMAP na domyślnym porcie 993.

Przykładowe użycie:

.. code-block:: python
   :linenos:

   import imaplib

   # Nawiązanie połączenia z serwerem IMAP przez SSL/TLS
   imap_connection = imaplib.IMAP4_SSL('mail.example.com')

   # Autoryzacja na serwerze IMAP
   imap_connection.login('username', 'password')

   # Wykonanie operacji na skrzynce pocztowej
   # np. pobranie listy folderów, pobranie wiadomości, itp.

   # Zamknięcie połączenia
   imap_connection.logout()

W tym przykładzie tworzymy obiekt imap_connection poprzez wywołanie funkcji
`imaplib.IMAP4_SSL('mail.example.com')`-Python, gdzie 'mail.example.com' jest adresem hosta serwera IMAP.
Następnie autoryzujemy się na serwerze poprzez metodę login, używając nazwy użytkownika i hasła.
Po zakończeniu operacji na skrzynce pocztowej zaleca się zamknięcie połączenia za pomocą metody logout.
