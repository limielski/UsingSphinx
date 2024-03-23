Operacje na skrzynce i mailach
==============================

Sekcja "# Wykonanie operacji na skrzynce pocztowej" patrz listing poniżej listing_ , zaznaczone na żółto, obejmuje operacje, które można wykonać na skrzynce pocztowej po nawiązaniu połączenia z serwerem IMAP przez SSL/TLS. Te operacje mogą obejmować różne zadania, takie jak pobieranie listy folderów, pobieranie wiadomości e-mail, wysyłanie nowych wiadomości, usuwanie wiadomości, przesuwanie wiadomości między folderami, itp.

W protokole IMAP (Internet Message Access Protocol), każda wiadomość w folderze skrzynki pocztowej ma przypisany unikalny identyfikator UID (Unique Identifier). UID jest to liczba całkowita przypisana do każdej wiadomości w folderze, która służy do jednoznacznego identyfikowania tej wiadomości w kontekście danego folderu. UID jest stały dla danej wiadomości w danym folderze, co oznacza, że pozostaje niezmieniony nawet po dodaniu lub usunięciu innych wiadomości.

UID umożliwia wykonywanie operacji na wiadomościach w sposób bardziej niezależny od ich numerów sekwencyjnych (Sequence Numbers), które mogą ulec zmianie w wyniku dodawania lub usuwania wiadomości z foldera. Dzięki UID możliwe jest precyzyjne odwoływanie się do konkretnych wiadomości bez obaw o zmianę numerów sekwencyjnych.

Aby uzyskać unikalny UID dla danej wiadomości, można użyć metody fetch() wraz z odpowiednimi parametrami w module imaplib. Większość serwerów IMAP automatycznie generuje unikalne UID dla każdej wiadomości podczas ich dostarczania do skrzynki pocztowej. O tym w sekcji `Funkcja uid()`_

Numery sekwencyjne (Sequence Numbers) to kolejne liczby całkowite przypisane do każdej wiadomości w danym folderze, zaczynając od 1 dla pierwszej wiadomości, 2 dla drugiej, itd. Numery sekwencyjne mogą ulec zmianie w wyniku dodawania nowych wiadomości do foldera lub usuwania istniejących. Są one używane w niektórych operacjach IMAP, takich jak wyszukiwanie wiadomości, ale mogą być mniej stabilne niż UID, dlatego też UID są preferowanym sposobem identyfikowania wiadomości.

.. _listing:

.. code-block:: python
   :emphasize-lines: 9, 10
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

W przypadku odczytu wiadomości e-mail, najczęściej używane operacje to:

Możemy użyć metody list() obiektu imap_connection, aby pobrać listę dostępnych folderów na serwerze IMAP.

.. code-block::python
   :linenos:

   folders_status, folders_list = imap_connection.list()
   print("Lista folderów:")
   for folder in folders_list:
       print(folder)

Pobieranie listy wiadomości
---------------------------

Możemy użyć metody select() obiektu imap_connection, aby wybrać folder, a następnie użyć metody search() do wyszukiwania wiadomości w wybranym folderze. Na przykład:

.. code-block::
   :linenos:

   # Wybierz folder "INBOX"
   status, data = imap_connection.select("INBOX")

   # Znajdź wszystkie wiadomości w folderze "INBOX"
   status, msg_ids = imap_connection.search(None, 'ALL')

   # Pobierz nagłówki wiadomości
   for msg_id in msg_ids[0].split():
       status, msg_data = imap_connection.fetch(msg_id, '(RFC822.HEADER)')
       print(msg_data[0][1])

Funkcja fetch
-------------

Funkcja `fetch()` w protokole IMAP służy do pobierania danych konkretnych wiadomości na podstawie ich identyfikatorów (UID lub numerów sekwencyjnych). Głównym celem tej funkcji jest pobranie treści, nagłówków lub innych danych z określonych wiadomości.

Oto opis tej funkcji oraz możliwe wartości parametrów:

1. Pierwszy parametr (message_set):
   - Wartość: Ciąg znaków reprezentujący identyfikatory wiadomości (UID lub numery sekwencyjne) lub zakres tych identyfikatorów.
   - Opis: Określa, które wiadomości mają zostać pobrane. Możesz podać pojedynczy numer wiadomości, listę numerów lub zakres numerów. Na przykład `1`, `1:5`, `2,4,6`.

2. Drugi parametr (data_items):
   - Wartość: Ciąg znaków reprezentujący żądane dane do pobrania.
   - Opis: Określa, jakie konkretne dane chcesz pobrać z wiadomości. Możesz pobrać treść wiadomości, nagłówki, załączniki itp. Poprawny format tego parametru zależy od implementacji biblioteki IMAP i może zawierać różne opcje. Najczęściej używaną opcją jest `(RFC822)`, która pobiera treść i nagłówki wiadomości.

Przykładowe wartości parametru `data_items`:
- `(RFC822)`: Pobiera treść i nagłówki wiadomości.
- `BODY[HEADER]`: Pobiera jedynie nagłówki wiadomości.
- `BODY[TEXT]`: Pobiera jedynie treść wiadomości.

Przykład użycia funkcji `fetch()`:

```python
# Pobierz treść i nagłówki wiadomości o numerze UID 1
resp_code, mail_data = imap_ssl.fetch('1', '(RFC822)')
```

W tym przykładzie używamy funkcji `fetch()` w celu pobrania treści i nagłówków wiadomości o numerze UID równym 1. Otrzymane dane zostaną zwrócone jako wynik operacji.

Pobranie treści wiadomości
~~~~~~~~~~~~~~~~~~~~~~~~~~


Po znalezieniu interesującej nas wiadomości, możemy użyć metody fetch() do pobrania pełnej treści wiadomości.

.. code-block::
   :linenos:

   # Pobierz treść wiadomości o określonym identyfikatorze
   status, msg_data = imap_connection.fetch('1', '(RFC822)')
   email_body = msg_data[0][1]
   print(email_body.decode('utf-8'))

Pobieranie nagłówków wiadomości
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aby uzyskać dostęp tylko do nagłówków wiadomości bez pobierania całej treści, możemy użyć metody fetch() z odpowiednimi argumentami.

.. code-block::
   :linenos:

   # Pobierz nagłówki wiadomości o określonym identyfikatorze
   status, msg_data = imap_connection.fetch('1', '(BODY[HEADER])')
   email_header = msg_data[0][1]
   print(email_header.decode('utf-8'))


Funkcja search
--------------

Funkcja `imap_ssl.search(None, "ALL")` służy do wyszukiwania wiadomości w skrzynce pocztowej na podstawie określonych kryteriów. Głównym celem jest zwrócenie identyfikatorów (numery UID lub numery sekwencyjne) wiadomości spełniających podane kryteria wyszukiwania. Gdy wywołujesz tę funkcję z argumentami `None` i `"ALL"`, oznacza to, że chcesz pobrać wszystkie wiadomości znajdujące się w skrzynce pocztowej.

Oto opis parametrów tej funkcji oraz możliwe wartości:

1. Pierwszy parametr (mailbox):
   - Wartość: `None` lub nazwa skrzynki pocztowej.
   - Opis: Określa skrzynkę pocztową, w której chcesz przeprowadzić wyszukiwanie. Jeśli wartość to `None`, wyszukiwanie będzie prowadzone w aktualnie wybranej skrzynce.

2. Drugi parametr (criteria):
   - Wartość: Ciąg znaków reprezentujący kryteria wyszukiwania.
   - Opis: Określa kryteria, na podstawie których chcesz wyszukać wiadomości. Możesz użyć różnych kryteriów wyszukiwania, takich jak `ALL` (wszystkie wiadomości), `UNSEEN` (nieprzeczytane wiadomości), `FROM`, `TO`, `SUBJECT`, `SINCE`, `BEFORE` itp.

Przykładowe wartości parametru `criteria`:
- `"ALL"`: Wyszukuje wszystkie wiadomości w skrzynce pocztowej.
- `"UNSEEN"`: Wyszukuje nieprzeczytane wiadomości.
- `"FROM example@example.com"`: Wyszukuje wiadomości, których nadawcą jest określony adres e-mail.
- `"SINCE 1-Jan-2023"`: Wyszukuje wiadomości wysłane po określonej dacie.

Oczywiście, istnieją też bardziej złożone kryteria wyszukiwania, które można łączyć w celu bardziej szczegółowego wyszukiwania. Jednak używając `"ALL"`, jak w Twoim przykładzie, otrzymasz wszystkie wiadomości znajdujące się w skrzynce pocztowej.


Usuwanie wiadomości
-------------------

Aby usunąć wiadomość z folderu, możemy użyć metody store() z odpowiednimi argumentami

.. code-block::
   :linenos:

   # Usuń wiadomość o określonym identyfikatorze
   status, data = imap_connection.store('1', '+FLAGS', '\\Deleted')
   imap_connection.expunge()

Przesuwanie wiadomości
----------------------

Aby przenieść wiadomość z jednego folderu do drugiego, możemy użyć metody copy() w połączeniu z store() i expunge().

.. code-block::
   :linenos:

   # Przenieś wiadomość o określonym identyfikatorze do innego folderu
   status, data = imap_connection.copy('1', 'Archive')
   imap_connection.store('1', '+FLAGS', '\\Deleted')
   imap_connection.expunge()

Wysyłanie nowej wiadomości
--------------------------

.. code-block::pton
   :linenos:

   import smtplib
   from email.mime.text import MIMEText

   # Tworzenie treści wiadomości
   msg = MIMEText('Treść wiadomości')
   msg['Subject'] = 'Temat wiadomości'
   msg['From'] = 'nadawca@example.com'
   msg['To'] = 'odbiorca@example.com'

   # Ustanowienie połączenia z serwerem SMTP
   smtp_connection = smtplib.SMTP('smtp.example.com')
   smtp_connection.starttls()  # Rozpoczęcie trybu TLS (opcjonalne)

   # Autoryzacja na serwerze SMTP (opcjonalne)
   smtp_connection.login('username', 'password')

   # Wysłanie wiadomości
   smtp_connection.sendmail('nadawca@example.com', ['odbiorca@example.com'], msg.as_string())

   # Zamknięcie połączenia
   smtp_connection.quit()

Odpowiadanie na wiadomość
-------------------------

Aby odpowiedzieć na otrzymaną wiadomość e-mail, możemy użyć metody reply()

.. code-block:: python
   :linenos:

   # Odpowiedź na wiadomość o określonym identyfikatorze
   status, msg_data = imap_connection.fetch('1', '(RFC822)')
   original_email = msg_data[0][1]

   # Przygotowanie treści odpowiedzi
   reply_message = MIMEText('Treść odpowiedzi')
   reply_message['Subject'] = 'Re: Temat wiadomości'
   reply_message['From'] = 'nadawca@example.com'
   reply_message['To'] = 'nadawca@example.com'  # Odpowiedź do nadawcy oryginalnej wiadomości

   # Wysłanie odpowiedzi
   smtp_connection.sendmail('nadawca@example.com', ['nadawca@example.com'], reply_message.as_string())

Przeszukiwanie wiadomości
-------------------------

Aby przeszukać wiadomości w folderze pod kątem określonych kryteriów, możemy użyć metody search()

.. code-block:: python
   :linenos:

   # Przeszukaj wiadomości w folderze "INBOX" dla określonego
   # kryterium(np. zawierających określone słowo kluczowe)

   status, msg_ids = imap_connection.search(None, 'BODY "kluczowe_słowo"')

Pobieranie załączników
----------------------

.. code-block:: python
   :linenos:

   import email

   # Pobierz treść wiadomości
   status, msg_data = imap_connection.fetch('1', '(RFC822)')
   email_body = msg_data[0][1]

   # Przetwarzanie treści wiadomości
   msg = email.message_from_bytes(email_body)

   # Pobierz załączniki
   for part in msg.walk():
       if part.get_content_maintype() == 'multipart':
           continue
       if part.get('Content-Disposition') is None:
           continue
       filename = part.get_filename()
       if filename:
           with open(filename, 'wb') as f:
               f.write(part.get_payload(decode=True))




Funkcja uid()
=============

W  przykładach używamy metody uid() zamiast standardowych operacji, takich jak search, fetch, store, itp.
Metoda uid() umożliwia operowanie na wiadomościach za pomocą ich unikalnych identyfikatorów UID zamiast numerów sekwencyjnych. Dzięki temu możemy bardziej precyzyjnie zarządzać wiadomościami, szczególnie w przypadku, gdy zachodzi potrzeba operowania na wiadomościach w sposób nieliniowy.

mail.uid(command, argument, msg_set)

W kontekście metody mail.uid z pakietu imaplib, argumenty mogą być ogólnie opisane w następujący sposób:

command: Jest to polecenie IMAP4rev1 UID, które ma zostać wykonane.
Przykłady to SEARCH, FETCH, STORE, COPY, i MOVE.

argument: Zależy od polecenia, ale zazwyczaj jest to identyfikator wiadomości, do której ma zostać zastosowane polecenie (ID wiadomości, zakres ID lub lista ID), lub None w przypadku polecenia SEARCH.

message_set lub search_criterion lub data (zależy od polecenia): Jest to argument specyficzny dla polecenia, który określa, jakie dane mają być przetwarzane.
Dla SEARCH, będzie to kryterium wyszukiwania.
Dla FETCH, będzie to część wiadomości do pobrania.
Dla STOR', będą to flagi do zmiany.
Dla COPY i MOVE, będzie to nazwa skrzynki docelowej.


Trzeci argument w mail.uid jest zależny od polecenia, jakie chcesz wykonać. Poniżej znajduje się także krótka tabelka z wyjaśnieniem:

+---------------------------------------------------------------+
| Polecenie | Opis                                              |
+===========+===================================================+
| SEARCH    | Wyszukuje wiadomości spełniające kryteria.        |
+-----------+---------------------------------------------------+
| FETCH     | Pobiera konkretną porcję danych wiadomości.       |
+-----------+---------------------------------------------------+
| STORE     | Modyfikuje flagi wiadomości.                      |
+-----------+---------------------------------------------------+
| COPY      | Kopiuje wiadomości z bieżącego skrzynki do innej. |
+-----------+---------------------------------------------------+
| MOVE      | Przenosi wiadomości z bieżącego skrzynki do innej.|
+-----------+---------------------------------------------------+

W przypadku \"FETCH", \"STORE", \"COPY", i \"MOVE" drugi argument metody uid jest używany do przekazania zakresu wiadomości, do których ma zastosowanie polecenie.

Zakres ten jest reprezentowany jako ciąg, i może obejmować jeden UID(\"1"), zakres UID (\"1:"), lub wielokrotny UID oddzielony przecinkami (\"1,3").
Na przykład:

.. code-block:: python
   :linenos:

   mail.uid("STORE", "1", "+FLAGS (\\Deleted)") # Oznacza wiadomość o UID 1 jako usuniętą.
   mail.uid("FETCH", "1", "(BODY[TEXT])") # Pobiera treść wiadomości o UID 1.
   mail.uid("COPY", "1", "INBOX") # Kopiuje wiadomość o UID 1 do skrzynki odczytanej.
   mail.uid("MOVE", "1", "INBOX") # Przenosi wiadomość o UID 1 do skrzynki odczytanej.


Pamiętaj, że te polecenia IMAP są skierowane do serwera, więc rzeczywistość ich działania może zależeć od konkretnego serwera i jego konfiguracji.

Pobieranie listy folderów za pomocą UID:
----------------------------------------

.. code-block:: python
   :linenos:

   # Pobierz listę folderów za pomocą UID
   status, folders_list = imap_connection.uid('list', '""', '*')
   print("Lista folderów:")
   for folder in folders_list[1].splitlines():
       print(folder.decode())

Pobieranie listy wiadomości w folderze
--------------------------------------

.. code-block:: python
   :linenos:

   # Wybierz folder "INBOX" za pomocą UID
   status, folder_data = imap_connection.select('INBOX')
   # Pobierz listę UID wiadomości w folderze "INBOX"
   status, msg_uids = imap_connection.uid('search', None, 'ALL')
   print("Lista UID wiadomości:")
   print(msg_uids[0].decode())

Pobieranie treści wiadomości
----------------------------

.. code-block:: python
   :linenos:

   # Pobierz treść wiadomości o określonym UID
   status, msg_data = imap_connection.uid('fetch', '1', '(RFC822)')
   email_body = msg_data[1][0][1]
   print(email_body.decode('utf-8'))

Usuwanie wiadomości
-------------------

.. code-block:: python
   :linenos:

   # Usuń wiadomość o określonym UID
   status, data = imap_connection.uid('store', '1', '+FLAGS', '\\Deleted')
   imap_connection.expunge()

Przesuwanie wiadomości między folderami
---------------------------------------

.. code-block:: python
   :linenos:

   # Przenieś wiadomość o określonym UID do innego folderu
   status, data = imap_connection.uid('copy', '1', 'Archive')
   # Oznacz wiadomość jako usuniętą w folderze źródłowym
   status, data = imap_connection.uid('store', '1', '+FLAGS', '\\Deleted')
   # Usuń wiadomości oznaczone jako usunięte
   imap_connection.expunge()

Czytanie poczty i jej wyświetlanie
==================================

.. code-block:: python
   :linenos:

   import imaplib

   # Dane logowania
   email_address = 'twoj_adres_email@gmail.com'
   password = 'twoje_haslo'

   # Adres serwera IMAP i port
   imap_server = 'imap.gmail.com'
   port = 993

   # Tworzenie połączenia z serwerem IMAP
   imap_connection = imaplib.IMAP4_SSL(imap_server, port)

   # Logowanie do skrzynki pocztowej
   imap_connection.login(email_address, password)

   # Wybór folderu (np. "INBOX")
   folder = 'INBOX'
   imap_connection.select(folder)

   # Pobranie listy UID wiadomości w folderze
   status, msg_uids = imap_connection.uid('search', None, 'ALL')

   # Sprawdzenie, czy udało się pobrać listę UID
   if status == 'OK':
       # Przetwarzanie listy UID
       msg_uids_list = msg_uids[0].split()
       for uid in msg_uids_list:
           # Pobieranie treści wiadomości o danym UID
           status, msg_data = imap_connection.uid('fetch', uid, '(RFC822)')
           email_body = msg_data[1][0][1]
           print(f"UID: {uid.decode()}")
           print(email_body.decode('utf-8'))

   # Zamknięcie połączenia
   imap_connection.logout()


Analiza kodu
------------

Przeanalizujmy ten kod krok po kroku:

1. :python:`status, msg_uids = imap_connection.uid('search', None, 'ALL')`: Ta linia kodu wysyła zapytanie do serwera IMAP o pobranie listy UID wszystkich wiadomości w aktualnie wybranym folderze (w tym przypadku \"INBOX"). Metoda :python:`uid()` służy do operacji na wiadomościach przy użyciu ich UID. Wynik tej operacji zawiera listę UID wiadomości, które są przechowywane w zmiennej :python:`msg_uids`.

2. :python:`if status == 'OK':`: Ten warunek sprawdza, czy operacja pobrania listy UID zakończyła się sukcesem. Jeśli status odpowiedzi serwera IMAP to :python:`'OK'`, oznacza to, że operacja została wykonana poprawnie.

3. :python:`msg_uids_list = msg_uids[0].split()`: Ta linia kodu przetwarza wynik operacji :python:`uid('search')`, który jest w postaci łańcucha znaków zawierającego listę UID wiadomości, oddzielonych spacjami. Metoda :python:`split()` dzieli ten łańcuch na poszczególne UID i przechowuje je w liście :python:`msg_uids_list`.

.. hint::
   wynik operacji :python:`uid('search')`, przechowywany w zmiennej msg_uids, jest jednowymiarową listą zawierającą tylko jeden element, który jest łańcuchem znaków reprezentującym listę UID wiadomości. Zatem indeksowanie :python:`msg_uids[0]` jest jedynym sposobem uzyskania tego łańcucha znaków.

4. :python:`for uid in msg_uids_list:`: Ta pętla iteruje po każdym UID w liście :python:`msg_uids_list`.

5. :python:`status, msg_data = imap_connection.uid('fetch', uid, '(RFC822)')`: W tej linii kodu pobieramy treść wiadomości o określonym UID z serwera IMAP za pomocą metody :python:`uid('fetch')`. Parametr :python:`(RFC822)` wskazuje, że chcemy pobrać pełną treść wiadomości w formacie RFC822, który zawiera nagłówki i treść wiadomości. Wynik tej operacji zawiera status odpowiedzi serwera IMAP oraz dane wiadomości, przechowywane w zmiennej :python:`msg_data`.

6. :python:`email_body = msg_data[1][0][1]`: Tutaj pobieramy samą treść wiadomości z danych wiadomości przechowywanych w zmiennej :python:`msg_data`. Wiadomość jest przechowywana w postaci bajtów, dlatego też używamy indeksowania, aby uzyskać dostęp do treści.

.. hint::
   w przypadku protokołu IMAP, dane wiadomości, zwrócone przez metodę `uid('fetch')`, są przechowywane w formie krotek (tuple). Każda krotka zawiera nagłówek i treść wiadomości w postaci bajtów. Dokładniej:

   `msg_data` jest listą krotek, gdzie każda krotka reprezentuje jedną wiadomość.
   Wewnętrzna struktura każdej krotki wygląda tak: `(<typ_nagłówka>, <treść_wiadomości>)`.

   Tutaj, `msg_data[1][0][1]` odnosi się do treści wiadomości. Poniżej krótkie wyjaśnienie:

   * msg_data[1]: Odnosi się do drugiej krotki w liście msg_data, ponieważ w Pythonie indeksowanie zaczyna się od zera.
      * [0]: Odnosi się do pierwszego elementu w tej krotce, którym jest nagłówek.
      * [1]: Odnosi się do drugiego elementu w tej krotce, którym jest treść wiadomości w postaci bajtów.

7. :python:`print(f"UID: {uid.decode()}")`: Wyświetlamy UID wiadomości w formacie tekstowym, korzystając z metody :python:`decode()`, ponieważ UID jest przechowywane jako bajty, a chcemy wyświetlić je jako tekst.

8. :python:`print(email_body.decode('utf-8'))`: Wyświetlamy treść wiadomości w formacie tekstowym, korzystając z metody `decode()` do przekształcenia bajtów na tekst. Używamy kodowania 'utf-8', ponieważ jest to powszechne kodowanie dla treści e-mail.

9. :python:`imap_connection.logout()`: Na koniec zamykamy połączenie z serwerem IMAP, aby zwolnić zasoby i upewnić się, że sesja została prawidłowo zakończona.
