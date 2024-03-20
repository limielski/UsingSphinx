Funkcja mail.uid
----------------

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
