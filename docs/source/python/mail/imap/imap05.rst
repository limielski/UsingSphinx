Opis funkcji
============

.. role:: python(code)
   :language: python

imaplib.IMAP4_SSL(host, port)
-----------------------------

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


Potem po nawiazaniu połączenia przychodzi czas na zalogowanie się
jako USER_NAME i PASSWORD za pomocą funkcji login

Funkcja login
-------------

Funkcja login odnosi się do operacji uwierzytelniania podczas połączenia z serwerem poczty e-mail. Jest to często używane w kontekście bibliotek do obsługi protokołów pocztowych, takich jak smtplib w języku Python.

Oto ogólny opis funkcji login:

Cel funkcji: Uwierzytelnienie klienta w serwerze poczty e-mail.

Użycie: Funkcję mail.login stosuje się w scenariuszach, gdzie klient chce wysłać wiadomość e-mail przez serwer poczty e-mail. Przed wysłaniem wiadomości klient musi się zalogować, aby serwer potwierdził jego tożsamość i uprawnienia do wysyłania.

Argumenty: Funkcja może przyjmować różne argumenty zależnie od używanej biblioteki do obsługi poczty e-mail. Typowe argumenty obejmują nazwę użytkownika (adres e-mail) i hasło, które są wymagane do uwierzytelnienia.

Zwracana wartość: Jeśli uwierzytelnienie powiedzie się, funkcja login zwraca potwierdzenie zalogowania się do serwera. W przypadku niepowodzenia może zwrócić błąd lub wyjątek, w zależności od implementacji biblioteki.


W kontekście protokołu IMAP (Internet Message Access Protocol), funkcja mail.login służy do uwierzytelnienia klienta (czyli programu lub aplikacji) w serwerze IMAP. Pozwala to klientowi uzyskać dostęp do swoich skrzynek pocztowych i operować na wiadomościach e-mail znajdujących się na serwerze.

Ogólnie rzecz biorąc, aby użyć funkcji mail.login w kontekście IMAP, należy podać nazwę użytkownika (adres e-mail) oraz hasło, które są wymagane do uwierzytelnienia klienta na serwerze IMAP.

Poniżej przedstawiam przykład użycia funkcji mail.login w kontekście biblioteki imaplib w Pythonie, która umożliwia obsługę protokołu IMAP:

.. code-block:: python
   :emphasize-lines: 7
   :linenos:

   IMAP_SERVER = 'imap.example.com'
   IMAP_PORT = 993
   USERNAME = 'your_username'
   PASSWORD = 'your_password'

   mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
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

Po zalogowaniu sie przychodzi pora na dokonywanie operacji na skrzynkach i mailach
Możesz wykonywać operacje na skrzynce pocztowej, takie jak pobieranie wiadomości e-mail,
czy działania na skrzynkach jak usuwanie, dodawanie itp ...
